import os
import json
import sys
from pathlib import Path
from typing import Any, Optional

def ensure_directory(path: str) -> None:
    """Creates a directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def load_json_file(file_path: str) -> dict[str, Any]:
    """Reads and parses a JSON configuration file."""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_json_file(data: dict[str, Any], file_path: str) -> bool:
    """Serializes dictionary data into a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback."""
    return os.getenv(key, default) or ''

def exit_with_message(message: str, code: int = 1) -> None:
    """Prints message to stderr and terminates process."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(code)