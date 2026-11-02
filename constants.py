from typing import Final, Dict, List

# Application configuration constants for cli-helper-26
VERSION: Final[str] = "1.0.0"
TIMEOUT_SECONDS: Final[int] = 30
DEFAULT_ENCODING: Final[str] = "utf-8"

# Supported command patterns for internal processing
SUPPORTED_COMMANDS: Final[List[str]] = ["init", "run", "status", "cleanup"]

# Configuration paths mapping
PATH_MAP: Final[Dict[str, str]] = {
    "config": "~/.config/cli-helper/",
    "logs": "/var/log/cli-helper/",
    "cache": "/tmp/cli-helper/"
}

def get_timeout_buffer() -> int:
    """
    Calculate buffer based on system timeout settings.

    Returns:
        int: Calculated integer buffer value.
    """
    return TIMEOUT_SECONDS + 5
