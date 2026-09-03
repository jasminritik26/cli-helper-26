import json
from typing import Any, Dict, Optional

def safe_json_load(file_path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file with error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionaries for flat-file storage."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_input(value: Any) -> str:
    """Converts varied input types into sanitized strings."""
    if value is None:
        return ""
    return str(value).strip()

def batch_process(data: list, batch_size: int = 10):
    """Generator yielding batches from a larger list."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]