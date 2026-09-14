from typing import Final, Dict, List

# Application configuration constants for cli-helper-26
VERSION: Final[str] = "1.0.0"
DEFAULT_TIMEOUT: Final[int] = 30

# Allowed command configurations
SUPPORTED_COMMANDS: List[str] = ["init", "run", "status", "cleanup"]

# Status code mappings for CLI operations
STATUS_CODES: Dict[str, int] = {
    "SUCCESS": 0,
    "ERROR_UNKNOWN": 1,
    "ERROR_PERMISSION": 2,
    "ERROR_CONFIG": 3
}

# Default settings for output formatting
BUFFER_SIZE: Final[int] = 1024
LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def get_status_message(code: int) -> str:
    """Return a descriptive message for a given status code."""
    messages: Dict[int, str] = {
        0: "Operation completed successfully",
        1: "An unknown error occurred",
        2: "Permission denied during execution",
        3: "Configuration file is invalid"
    }
    return messages.get(code, "Unknown status code encountered")