import os
import json
import sys
from typing import Any, Optional

def load_json(filepath: str) -> Optional[dict]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json(filepath: str, data: dict) -> bool:
    """Serializes data to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def ensure_dir(directory: str) -> None:
    """Creates a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_input(prompt: str, default: Any = None) -> str:
    """Handles standard input with optional default values."""
    user_input = input(f"{prompt} [{default}]: ").strip()
    return user_input if user_input else str(default)

def exit_with_msg(message: str, code: int = 1) -> None:
    """Graceful script termination with status message."""
    print(message)
    sys.exit(code)