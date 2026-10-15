import os
from pathlib import Path

# Application path configurations
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_LOG_DIR = BASE_DIR / "logs"

# CLI environment constraints
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
SUPPORTED_EXTENSIONS = {'.json', '.yaml', '.yml', '.csv'}

# System environment variables
APP_NAME = "cli-helper-26"
DEBUG_MODE = os.getenv("DEBUG", "false").lower() == "true"

# Display configuration
TERMINAL_WIDTH = 80
COLOR_SCHEME = {
    "info": "cyan",
    "error": "red",
    "success": "green",
    "warning": "yellow"
}

# Operation limits
BATCH_SIZE = 100
CHUNK_SIZE = 4096