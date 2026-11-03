import json
import os
from typing import Any, Optional

def load_json_data(file_path: str) -> Optional[dict]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json_data(data: Any, file_path: str) -> bool:
    """Serializes data to a JSON file safely."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (TypeError, IOError):
        return False

def clean_dict(data: dict) -> dict:
    """Removes null entries from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}

def format_byte_size(size: int) -> str:
    """Converts bytes to a human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"