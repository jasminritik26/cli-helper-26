import logging

# Configuration constants for cli-helper-26
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

# Error message mapping for user-facing feedback
ERROR_MESSAGES = {
    "connection_error": "Failed to establish connection. Check your network.",
    "timeout_error": "Operation timed out after {} seconds.",
    "validation_error": "Input data validation failed.",
    "internal_error": "An unexpected internal error occurred.",
}

# Valid log levels mapping
LOG_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}

# Application path defaults
DEFAULT_CONFIG_PATH = "~/.config/cli-helper/config.json"
DEFAULT_LOG_PATH = "/var/log/cli-helper.log"

# Constraint constants
MIN_BUFFER_SIZE = 1024
MAX_BUFFER_SIZE = 65536

def get_error_message(key, *args):
    """Retrieve formatted error messages safely."""
    template = ERROR_MESSAGES.get(key, ERROR_MESSAGES["internal_error"])
    try:
        return template.format(*args)
    except (IndexError, TypeError):
        return template
