import os
import psycopg2
from psycopg2.extras import RealDictCursor
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("postgres_server")

@mcp.tool()
def query_db(sql_query: str) -> str:
    """Execute a read-only SQL SELECT query on the PostgreSQL database."""
    # Basic safety check (should be supplemented by DB user permissions in prod)
    if not sql_query.strip().upper().startswith("SELECT"):
        return "Error: For safety, only SELECT queries are allowed."
        
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        return "Error: DATABASE_URL environment variable is not set."

    try:
        # Connect to DB
        with psycopg2.connect(db_url) as conn:
            # Enforce read-only transaction context
            conn.readonly = True
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(sql_query)
                results = cur.fetchall()
                # Return stringified representation of the results
                return str(results)
    except Exception as e:
        return f"Database Error: {e}"

if __name__ == "__main__":
    # MCP servers communicate via standard input/output streams
    mcp.run(transport="stdio")
