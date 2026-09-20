import json
import os
from typing import Any, Dict, Optional

def safe_parse_json(content: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Parse JSON string safely, returning default on malformed data or empty string."""
    if not content or not isinstance(content, str) or not content.strip():
        return default if default is not None else {}
    
    try:
        data = json.loads(content)
        if isinstance(data, dict):
            return data
        return {"data": data}
    except (json.JSONDecodeError, TypeError, ValueError):
        return default if default is not None else {}

def safe_cast_int(value: Any, default: int = 0, min_val: Optional[int] = None, max_val: Optional[int] = None) -> int:
    """Safely cast value to integer with optional bounds checking."""
    try:
        parsed = int(float(value))
    except (TypeError, ValueError, OverflowError):
        return default

    if min_val is not None and parsed < min_val:
        return min_val
    if max_val is not None and parsed > max_val:
        return max_val
    return parsed

def get_env_var(key: str, default: str = "", required: bool = False) -> str:
    """Retrieve environment variable safely with optional enforcement."""
    val = os.getenv(key)
    if val is None or val.strip() == "":
        if required:
            raise ValueError(f"Required environment variable '{key}' is missing or empty")
        return default
    return val.strip()