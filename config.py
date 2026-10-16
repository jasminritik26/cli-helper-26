import os
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ConfigError(Exception):
    """Custom exception for configuration failures."""
    pass

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with error checking."""
    try:
        value = os.getenv(key, default)
        if value is None:
            raise ConfigError(f"Missing required configuration: {key}")
        return value
    except Exception as e:
        logger.error(f"Configuration retrieval failed for {key}: {str(e)}")
        raise ConfigError(f"Critical failure: {key} is not accessible") from e

def load_config_int(key: str, default_val: int) -> int:
    """Safely parses configuration value to integer."""
    raw_value = os.getenv(key)
    if raw_value is None:
        return default_val
    try:
        return int(raw_value)
    except (ValueError, TypeError) as e:
        logger.warning(f"Invalid integer format for {key}: {raw_value}. Using default: {default_val}")
        return default_val

def validate_path(path: str) -> bool:
    """Validates existence and accessibility of path."""
    if not path or not os.path.exists(path):
        logger.error(f"Invalid path provided: {path}")
        return False
    if not os.access(path, os.R_OK):
        logger.error(f"Insufficient read permissions for: {path}")
        return False
    return True