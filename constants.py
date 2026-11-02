import logging

# Configuration constants for cli-helper-26
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# Error handling constants
ERROR_EXIT_CODE = 1
SUCCESS_EXIT_CODE = 0

# Logging configuration
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.INFO

class ConfigError(Exception):
    """Base class for configuration edge cases."""
    pass

def get_retry_delay(attempt: int) -> float:
    """Calculates backoff delay for retries to prevent network flooding."""
    if not isinstance(attempt, int) or attempt < 0:
        return 1.0
    return float(2 ** attempt)

# Mapping for error status codes
STATUS_MAP = {
    "success": SUCCESS_EXIT_CODE,
    "error": ERROR_EXIT_CODE,
    "timeout": 2,
    "validation": 3
}