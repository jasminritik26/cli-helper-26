import json
import os
from typing import Any, Optional

def load_json_file(filepath: str) -> dict[str, Any]:
    """Loads and parses data from a local JSON file."""
    if not os.path.exists(filepath):
        return {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json_file(filepath: str, data: dict[str, Any]) -> bool:
    """Serializes data to a local JSON file with indentation."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        return True
    except (TypeError, IOError):
        return False

def sanitize_data(data: dict[str, Any]) -> dict[str, Any]:
    """Removes null entries from a dictionary recursively."""
    return {
        k: v for k, v in data.items()
        if v is not None and (not isinstance(v, dict) or sanitize_data(v))
    }