import os
import json
from typing import Any, Optional

def read_json(filepath: str) -> dict:
    """Load and parse json from a file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def write_json(filepath: str, data: Any) -> bool:
    """Serialize data to a json file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def ensure_dir(path: str) -> None:
    """Create directory path if not present."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieve environment variable with fallback."""
    return os.environ.get(key, default)

def format_byte_size(size_bytes: int) -> str:
    """Human readable string for byte sizes."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"