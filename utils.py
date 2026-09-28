import json
import os
from typing import Any, Optional

def load_json_file(file_path: str) -> dict[str, Any]:
    """Reads and parses a JSON file into a dictionary."""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json_file(data: dict[str, Any], file_path: str) -> bool:
    """Writes a dictionary to a JSON file formatted with indentation."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        return True
    except (TypeError, IOError):
        return False

def sanitize_input(value: Any) -> str:
    """Converts input to a stripped string safely."""
    if value is None:
        return ""
    return str(value).strip()

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback default."""
    return os.environ.get(key, default) or ""