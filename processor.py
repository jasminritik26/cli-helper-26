import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath: str, data: Dict[str, Any]) -> None:
    """Serializes data to a JSON file with indentation."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def get_timestamp() -> str:
    """Generates an ISO format timestamp string."""
    return datetime.now().isoformat()

def safe_get(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Retrieves a dictionary value with a fallback."""
    return data.get(key, default)

def format_byte_size(size_bytes: int) -> str:
    """Converts integer bytes to human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"

class DataProcessor:
    def __init__(self, settings: Optional[Dict] = None):
        self.settings = settings or {}

    def validate_keys(self, data: Dict, required: list) -> bool:
        """Checks if all required keys exist in dictionary."""
        return all(key in data for key in required)