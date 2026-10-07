import os
import json
import sys
from pathlib import Path
from typing import Any, Optional

def load_json(file_path: str) -> dict:
    """Read and parse a JSON file safely."""
    path = Path(file_path)
    if not path.exists():
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json(data: dict, file_path: str) -> bool:
    """Write data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def ensure_dir(dir_path: str) -> None:
    """Create directory path if it does not exist."""
    Path(dir_path).mkdir(parents=True, exist_ok=True)

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with fallback."""
    return os.environ.get(key, default or "")

def exit_with_msg(message: str, code: int = 1) -> None:
    """Print error and terminate execution."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(code)