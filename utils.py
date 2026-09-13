import json
import os
from typing import Any, Optional

def load_data(file_path: str) -> Optional[dict]:
    """Loads and parses JSON data from a file system path."""
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_data(data: Any, file_path: str) -> bool:
    """Serializes dictionary data to a JSON file safely."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        return True
    except (TypeError, IOError):
        return False

def sanitize_input(data: str) -> str:
    """Removes trailing whitespace and normalizes line endings."""
    if not isinstance(data, str):
        return ""
    return data.strip().replace('\r\n', '\n')

def format_byte_size(size_bytes: int) -> str:
    """Converts byte integer to human readable string format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"