import json
from typing import Any, Dict, Optional

def clean_data(data: Any) -> Any:
    """Recursively strips whitespace from string values in dicts/lists."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    elif isinstance(data, str):
        return data.strip()
    return data

def safe_load_json(file_path: str) -> Optional[Dict[str, Any]]:
    """Reads and cleans json file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return clean_data(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def format_output(data: Any, indent: int = 4) -> str:
    """Serializes data to formatted json string."""
    return json.dumps(data, indent=indent, sort_keys=True)

if __name__ == '__main__':
    # Example usage for verification
    sample = {" name ": "  developer  ", "items": ["  a ", " b  "]}
    print(format_output(clean_data(sample)))