import json
from typing import Any, Optional, Dict

def safe_load_json(file_path: str) -> Optional[Dict[str, Any]]:
    """Reads and parses a JSON file with basic error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        return None

def clean_data_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values from a dictionary recursively."""
    cleaned = {}
    for key, value in data.items():
        if isinstance(value, dict):
            nested = clean_data_dict(value)
            if nested:
                cleaned[key] = nested
        elif value is not None:
            cleaned[key] = value
    return cleaned

def format_output(data: Any, indent: int = 4) -> str:
    """Serializes data to a formatted JSON string."""
    try:
        return json.dumps(data, indent=indent, sort_keys=True)
    except (TypeError, ValueError):
        return str(data)