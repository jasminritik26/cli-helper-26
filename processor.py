import json
from typing import Any, Dict, Optional

def sanitize_data(data: Any) -> Any:
    """Recursively clean dictionary data for display or logging."""
    if isinstance(data, dict):
        return {str(k): sanitize_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data(i) for i in data]
    elif isinstance(data, (int, float, str, bool, type(None))):
        return data
    return str(data)

def load_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """Safely load and parse a JSON configuration file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def format_byte_size(size_bytes: int) -> str:
    """Convert integer byte size to human readable string."""
    if size_bytes == 0:
        return "0B"
    units = ("B", "KB", "MB", "GB", "TB")
    i = 0
    while size_bytes >= 1024 and i < len(units) - 1:
        size_bytes /= 1024
        i += 1
    return f"{size_bytes:.2f} {units[i]}"