import os
from pathlib import Path

# Application path definitions
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"

# CLI configuration defaults
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# Status codes for command operations
STATUS_SUCCESS = 0
STATUS_ERROR_GENERAL = 1
STATUS_ERROR_PERMISSION = 2
STATUS_ERROR_TIMEOUT = 3

# Supported file extensions
ALLOWED_EXTENSIONS = {".json", ".yaml", ".yml", ".toml"}

# Environment variables
ENV_PREFIX = "CLI_HELPER_"
DEBUG_MODE = os.getenv(f"{ENV_PREFIX}DEBUG", "false").lower() == "true"

# Formatting constants
HEADER_WIDTH = 80
DEFAULT_INDENT = 4

def get_version():
    return "2.6.0"

def get_log_path():
    LOG_DIR.mkdir(exist_ok=True)
    return LOG_DIR / "app.log"