import json
import os
import shutil
from typing import Any, Dict, Optional

def load_json_file(path: str) -> Dict[str, Any]:
    """Loads and parses a JSON file from disk."""
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(path: str, data: Dict[str, Any]) -> None:
    """Serializes dictionary data to a JSON file."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def safe_move(source: str, destination: str) -> bool:
    """Moves a file to a new location with existence check."""
    try:
        if os.path.exists(source):
            shutil.move(source, destination)
            return True
        return False
    except (IOError, shutil.Error):
        return False

def format_byte_size(size_bytes: int) -> str:
    """Converts raw bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable or returns default."""
    return os.environ.get(key, default or "")