import json
from typing import Any, Dict, Optional

def safe_load_json(file_path: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Reads a JSON file and returns data or a default value."""
    if default is None:
        default = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionaries for configuration or flat storage."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null entries from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}