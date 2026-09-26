import os
from pathlib import Path

# Application path definitions
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_LOG_DIR = BASE_DIR / "logs"
DEFAULT_CONFIG_PATH = BASE_DIR / "config.yaml"

# Timeouts and performance defaults
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 2

# Supported file extensions
SUPPORTED_EXTENSIONS = {'.json', '.yaml', '.yml', '.toml'}

# Environment variable keys
ENV_API_KEY = "CLI_HELPER_API_KEY"
ENV_LOG_LEVEL = "CLI_HELPER_LOG_LEVEL"

# Exit codes for cli operations
EXIT_SUCCESS = 0
EXIT_ERROR_GENERAL = 1
EXIT_ERROR_CONFIG = 2
EXIT_ERROR_NETWORK = 3

# User-facing CLI constants
APP_NAME = "cli-helper-26"
VERSION = "0.1.0"
BANNER = f"Initializing {APP_NAME} v{VERSION}..."

# Validation constraints
MIN_INPUT_LENGTH = 3
MAX_INPUT_LENGTH = 255