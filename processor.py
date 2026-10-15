import json
from typing import Any, Dict, Optional

def sanitize_data(data: Any) -> Any:
    """
    Recursively cleans input data for cli display.
    Ensures types are compatible with standard streams.
    """
    if isinstance(data, dict):
        return {str(k): sanitize_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(i) for i in data]
    if isinstance(data, (int, float, str, bool, type(None))):
        return data
    return str(data)

def format_json(data: Any, indent: int = 4) -> str:
    """
    Serializes data to a formatted json string.
    """
    try:
        return json.dumps(sanitize_data(data), indent=indent)
    except (TypeError, ValueError) as e:
        return f"Error processing data: {e}"

def load_json_file(filepath: str) -> Optional[Dict]:
    """
    Reads and parses a json configuration file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None