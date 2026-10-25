import json
import os
from typing import Any, Optional

def load_json_file(filepath: str) -> Optional[dict]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json_file(filepath: str, data: dict) -> bool:
    """Serializes dictionary to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        return True
    except (TypeError, IOError):
        return False

def sanitize_data(data: Any) -> Any:
    """Recursively strips whitespace from string values."""
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(i) for i in data]
    if isinstance(data, str):
        return data.strip()
    return data