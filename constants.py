import os
from pathlib import Path

# Application path configurations
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

# CLI environment defaults
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
APP_NAME = "cli-helper-26"

# Supported formats for operations
SUPPORTED_FORMATS = {".json", ".yaml", ".toml"}

# Error message templates
ERR_MISSING_CONFIG = "Configuration file not found in path."
ERR_INVALID_FORMAT = "The provided file format is not supported."

# UI theme constants
THEME_COLORS = {
    "info": "blue",
    "success": "green",
    "warning": "yellow",
    "error": "red"
}

def ensure_directories():
    """Initialize application filesystem structure."""
    for directory in [LOG_DIR, DATA_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

# Ensure environment readiness
ensure_directories()