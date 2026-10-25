import os
import json
import sys
from typing import Any, Optional

def read_json(file_path: str) -> dict:
    """Load and parse a JSON file safely."""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def write_json(file_path: str, data: dict) -> bool:
    """Write dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with fallback."""
    return os.environ.get(key, default or "")

def format_byte_size(size: int) -> str:
    """Convert bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def exit_with_msg(message: str, code: int = 1) -> None:
    """Print error and terminate execution."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(code)