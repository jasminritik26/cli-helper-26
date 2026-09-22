import json
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file into a dictionary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading {file_path}: {e}")
        return {}

def save_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """Serializes dictionary data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError as e:
        print(f"Error writing to {file_path}: {e}")
        return False

def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null entries from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}

def merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merges two configuration dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result