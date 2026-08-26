"""
Global constants and configuration values for cli-helper-26.

This module defines application-wide limits, default settings, and exit codes.
"""

from typing import Dict, Final

DEFAULT_TIMEOUT: Final[int] = 30
BUFFER_SIZE: Final[int] = 1024
APP_NAME: Final[str] = "cli-helper-26"
VERSION: Final[str] = "1.0.0"

EXIT_SUCCESS: Final[int] = 0
EXIT_FAILURE: Final[int] = 1
EXIT_INVALID_ARGS: Final[int] = 2

SUPPORTED_FORMATS: Final[Dict[str, str]] = {
    "json": "application/json",
    "yaml": "application/x-yaml",
    "text": "text/plain",
}

ERROR_MESSAGES: Final[Dict[int, str]] = {
    EXIT_SUCCESS: "Operation completed successfully.",
    EXIT_FAILURE: "An unexpected error occurred.",
    EXIT_INVALID_ARGS: "Invalid command line arguments provided.",
}
