import os
import sys
import json
from typing import Any, Dict, Optional

def load_json_file(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON configuration file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(filepath: str, data: Dict[str, Any]) -> bool:
    """Serialize data to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def ensure_directory(path: str) -> None:
    """Create directory structure if missing."""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Safe access to environment variables."""
    return os.environ.get(key, default)

def format_cli_output(message: str, level: str = 'INFO') -> str:
    """Standardized formatting for console messages."""
    return f"[{level.upper()}] {message}"

if __name__ == '__main__':
    # Basic validation of core functionality
    ensure_directory('data')
    print(format_cli_output('core modules initialized successfully'))