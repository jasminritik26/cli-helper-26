import json
from typing import Any, Optional

def safe_load_json(file_path: str) -> dict[str, Any]:
    """Reads and parses a JSON file into a dictionary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error accessing {file_path}: {e}")
        return {}

def sanitize_input(data: Any) -> Any:
    """Removes trailing whitespace from string values in nested data."""
    if isinstance(data, str):
        return data.strip()
    elif isinstance(data, dict):
        return {k: sanitize_input(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_input(i) for i in data]
    return data

def merge_configurations(base: dict, overrides: dict) -> dict:
    """Deep merge for configuration dictionaries."""
    result = base.copy()
    for key, value in overrides.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_configurations(result[key], value)
        else:
            result[key] = value
    return result