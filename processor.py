import json
import os
import shutil
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Loads data from a json file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], filepath: str) -> None:
    """Writes dictionary data to a json file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def safe_copy(src: str, dst: str) -> bool:
    """Copies file with exception handling."""
    try:
        shutil.copy2(src, dst)
        return True
    except (IOError, OSError):
        return False

def ensure_dir(directory: str) -> None:
    """Creates directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def format_bytes(size: int) -> str:
    """Converts byte size to human readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"