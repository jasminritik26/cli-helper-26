import json
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file into a dictionary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {}

def save_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """Serializes dictionary data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}

def format_byte_size(size: int) -> str:
    """Converts integer bytes into human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"