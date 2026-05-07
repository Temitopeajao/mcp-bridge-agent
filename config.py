import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    
    # Resolve absolute paths to the server scripts
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    POSTGRES_SERVER_PATH = os.path.join(BASE_DIR, "mcp_servers", "postgres_server.py")
    FILESYSTEM_SERVER_PATH = os.path.join(BASE_DIR, "mcp_servers", "filesystem_server.py")

config = Config()
