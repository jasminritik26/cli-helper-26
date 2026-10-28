import os

# Configuration paths and default settings for cli-helper-26
APP_NAME = "cli-helper-26"
VERSION = "1.0.0"

# Default directory paths
BASE_DIR = os.path.expanduser(f"~/.{APP_NAME}")
LOG_DIR = os.path.join(BASE_DIR, "logs")
CACHE_DIR = os.path.join(BASE_DIR, "cache")

# Execution defaults
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# Status codes for internal handlers
STATUS_SUCCESS = 0
STATUS_ERROR_GENERAL = 1
STATUS_ERROR_VALIDATION = 2
STATUS_ERROR_TIMEOUT = 3

# File extensions and formatting
SUPPORTED_FORMATS = {'.json', '.yaml', '.yml', '.toml'}
ENCODING = "utf-8"

# Logging configuration
LOG_FILE = os.path.join(LOG_DIR, "app.log")
LOG_LEVELS = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40
}

def ensure_dirs():
    """Initialize application filesystem structure."""
    for path in [LOG_DIR, CACHE_DIR]:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)