import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("filesystem_server")

@mcp.tool()
def read_file(filepath: str) -> str:
    """Read the complete contents of a file from the filesystem."""
    if not os.path.isfile(filepath):
        return f"Error: File '{filepath}' does not exist or is not a file."
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

@mcp.tool()
def list_directory(path: str) -> str:
    """List all files and subdirectories in the given directory path."""
    if not os.path.isdir(path):
        return f"Error: Directory '{path}' does not exist."
    try:
        items = os.listdir(path)
        return "\n".join(items) if items else "(Empty directory)"
    except Exception as e:
        return f"Error listing directory: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
