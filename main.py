import asyncio
import sys
import os
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from config import config

class MCPOrchestrator:
    def __init__(self):
        self.exit_stack = AsyncExitStack()
        self.sessions = {}  # Stores active MCP client sessions

    async def start_server(self, name: str, script_path: str):
        """Spawns an MCP server as a subprocess and establishes a session."""
        print(f"[{name}] Starting server...")
        
        # Pass the current environment so the DB server can see DATABASE_URL
        env = os.environ.copy()
        
        server_params = StdioServerParameters(
            command=sys.executable,  # Uses the current Python environment
            args=[script_path],
            env=env
        )
        
        # Initialize stdio transport and standard MCP session
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        read, write = stdio_transport
        session = await self.exit_stack.enter_async_context(ClientSession(read, write))
        
        await session.initialize()
        self.sessions[name] = session
        print(f"[{name}] Initialization complete.")

    async def list_all_tools(self):
        """Query all connected servers for their available tools."""
        all_tools = {}
        for name, session in self.sessions.items():
            response = await session.list_tools()
            all_tools[name] = response.tools
        return all_tools

    async def call_tool(self, server_name: str, tool_name: str, arguments: dict):
        """Invoke a specific tool on a specific server."""
        if server_name not in self.sessions:
            raise ValueError(f"Server '{server_name}' not found.")
        
        session = self.sessions[server_name]
        result = await session.call_tool(tool_name, arguments)
        
        # MCP responses can contain multiple content blocks (e.g., text, images). 
        # We extract all text blocks and combine them.
        text_outputs =[block.text for block in result.content if block.type == "text"]
        return "\n".join(text_outputs)

    async def cleanup(self):
        """Safely shut down all server subprocesses."""
        await self.exit_stack.aclose()


async def main():
    orchestrator = MCPOrchestrator()
    try:
        # 1. Boot up both MCP servers
        await orchestrator.start_server("postgres", config.POSTGRES_SERVER_PATH)
        await orchestrator.start_server("filesystem", config.FILESYSTEM_SERVER_PATH)

        # 2. Discover available tools dynamically
        tools = await orchestrator.list_all_tools()
        print("\n=== Discovered MCP Tools ===")
        for server_name, server_tools in tools.items():
            for t in server_tools:
                print(f"- [{server_name}] {t.name}: {t.description}")

        # 3. Execute Filesystem Tool
        print("\n=== Testing Filesystem: list_directory ===")
        # We list the files in the current working directory
        fs_result = await orchestrator.call_tool("filesystem", "list_directory", {"path": "."})
        print(fs_result)

        # 4. Execute PostgreSQL Tool
        print("\n=== Testing PostgreSQL: query_db ===")
        # Note: If no DB is running or credentials are wrong, this will print the Postgres error 
        # but the MCP tool execution itself will still gracefully succeed.
        pg_result = await orchestrator.call_tool(
            "postgres", 
            "query_db", 
            {"sql_query": "SELECT 1 as system_check;"}
        )
        print(pg_result)

    finally:
        print("\nShutting down servers...")
        await orchestrator.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
