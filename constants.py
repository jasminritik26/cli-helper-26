"""Global constants and configuration values for cli-helper-26."""

from typing import Dict, Final, List

# Application metadata
APP_NAME: Final[str] = "cli-helper-26"
APP_VERSION: Final[str] = "1.0.0"

# Exit codes
EXIT_SUCCESS: Final[int] = 0
EXIT_FAILURE: Final[int] = 1
EXIT_INVALID_ARGS: Final[int] = 2

# Supported command prefixes
COMMAND_PREFIXES: Final[List[str]] = ["--", "-"]

# Default configuration settings
DEFAULT_CONFIG: Final[Dict[str, str]] = {
    "verbosity": "info",
    "timeout": "30",
    "encoding": "utf-8",
}

# Maximum retry attempts for operations
MAX_RETRIES: Final[int] = 3

# Log format specification
LOG_FORMAT: Final[str] = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
