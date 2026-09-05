import os
import sys
from pathlib import Path

# Application configuration defaults
APP_NAME = "cli-helper-26"
DEFAULT_ENCODING = "utf-8"
LOG_LEVEL = "INFO"

# Directory structure definitions
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
CACHE_DIR = BASE_DIR / ".cache"

# System constraints and limits
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Formatting and UI constants
SUCCESS_PREFIX = "[+]"
ERROR_PREFIX = "[!]"
WARNING_PREFIX = "[*]"

# Environment configuration keys
ENV_VARS = {
    "API_KEY": "APP_API_KEY",
    "DEBUG_MODE": "APP_DEBUG",
    "STORAGE_PATH": "APP_STORAGE_PATH"
}

def ensure_directories():
    """Initializes mandatory directory structure for the application."""
    for directory in [LOG_DIR, CACHE_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

# Ensure environment readiness on import
ensure_directories()