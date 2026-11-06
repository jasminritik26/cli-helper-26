import os

# Application configuration constants
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Path and file system defaults
DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser('~'), '.cli-helper-26', 'config.json')
LOG_FILE_PATH = 'app.log'

# Error and status message strings
ERROR_MSG_TIMEOUT = "Operation timed out after {} seconds."
ERROR_MSG_FILE_ACCESS = "Insufficient permissions to access file: {}"
ERROR_MSG_INVALID_INPUT = "Provided input failed validation criteria."
STATUS_SUCCESS = "Operation completed successfully."

# Environment variable keys
ENV_API_KEY = "CLI_HELPER_API_KEY"
ENV_DEBUG_MODE = "CLI_HELPER_DEBUG"

def get_timeout_range():
    """Return tuple of default timeout settings."""
    return (5, TIMEOUT_SECONDS)

# Supported exit codes for error handling logic
EXIT_SUCCESS = 0
EXIT_INVALID_CONFIG = 1
EXIT_NETWORK_ERROR = 2
EXIT_PERMISSION_DENIED = 3