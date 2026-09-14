from typing import Final, Dict, List

# Application-wide configuration constants
VERSION: Final[str] = "0.1.0"
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Supported CLI operation modes
SUPPORTED_MODES: Final[List[str]] = ["init", "run", "status", "clean"]

# Exit code definitions for standard errors
EXIT_CODES: Final[Dict[str, int]] = {
    "SUCCESS": 0,
    "GENERAL_ERROR": 1,
    "INVALID_ARGUMENT": 2,
    "TIMEOUT_ERROR": 3
}

def get_timeout_threshold(factor: float = 1.0) -> float:
    """Calculates effective timeout based on a multiplier.

    Args:
        factor: A float to scale the default timeout value.

    Returns:
        The calculated timeout duration as a float.
    """
    return float(DEFAULT_TIMEOUT * factor)

# Placeholder for system path defaults
CACHE_DIR: Final[str] = "~/.cache/cli-helper-26"