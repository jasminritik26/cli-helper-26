import json
from typing import Any, Dict, Optional

def clean_data(data: Any) -> Any:
    """Recursively strips whitespace from string values in nested dictionaries."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_data(i) for i in data]
    elif isinstance(data, str):
        return data.strip()
    return data

def safe_load_json(file_path: str) -> Dict[str, Any]:
    """Reads and parses JSON file with error fallback."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return clean_data(data) if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def format_output(data: Any, indent: int = 4) -> str:
    """Serializes data to formatted JSON string."""
    return json.dumps(data, indent=indent, sort_keys=True)

def merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge for configuration dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result