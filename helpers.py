import os
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_read_file(filepath: str) -> Optional[str]:
    """Reads file content with robust error handling for missing files."""
    if not filepath:
        logger.error("invalid file path provided")
        return None

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        logger.warning(f"file not found: {filepath}")
    except PermissionError:
        logger.error(f"permission denied for: {filepath}")
    except OSError as e:
        logger.error(f"os error reading {filepath}: {e}")
    return None

def get_env_variable(key: str, default: Any = None) -> Any:
    """Fetches environment variable with fallback logic."""
    try:
        return os.environ.get(key, default)
    except Exception as e:
        logger.error(f"unexpected environment error for {key}: {e}")
        return default

def parse_input(data: Any) -> str:
    """Sanitizes and casts input data safely."""
    try:
        if data is None:
            return ""
        return str(data).strip()
    except (ValueError, TypeError) as e:
        logger.error(f"failed to cast data: {e}")
        return ""