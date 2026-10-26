import json
from typing import Any, Dict, Optional

def clean_data(data: Any) -> Any:
    """Recursively remove None values from dictionary."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [clean_data(v) for v in data]
    return data

def format_json(data: Any, indent: int = 4) -> str:
    """Serialize data to formatted string."""
    try:
        return json.dumps(data, indent=indent, sort_keys=True)
    except (TypeError, ValueError) as e:
        return f"Serialization error: {e}"

def safe_get(data: Dict, keys: str, default: Any = None) -> Any:
    """Access nested dictionary keys using dot notation."""
    parts = keys.split('.')
    current = data
    try:
        for part in parts:
            current = current[part]
        return current
    except (KeyError, TypeError):
        return default

def validate_schema(data: Dict, required_keys: list) -> bool:
    """Verify all keys exist in data dict."""
    return all(key in data for key in required_keys)