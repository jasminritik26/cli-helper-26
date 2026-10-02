import json
from typing import Any, Dict, List, Union


def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Recursively flatten a nested dictionary for easier CLI output display.

    Args:
        data: The dictionary to flatten.
        parent_key: Prefix for nested keys.
        sep: Separator between key levels.

    Returns:
        A single-level dictionary with flattened keys.
    """
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            for i, elem in enumerate(value):
                if isinstance(elem, dict):
                    items.extend(flatten_dict(elem, f"{new_key}[{i}]", sep=sep).items())
                else:
                    items.append((f"{new_key}[{i}]", elem))
        else:
            items.append((new_key, value))
    return dict(items)


def parse_kv_pairs(pairs: List[str]) -> Dict[str, str]:
    """Parse list of 'KEY=VALUE' strings passed from CLI flags into a dictionary.

    Args:
        pairs: List of raw CLI key-value strings.

    Returns:
        Parsed dictionary of key-value pairs.
    """
    result = {}
    for pair in pairs:
        if '=' in pair:
            key, val = pair.split('=', 1)
            result[key.strip()] = val.strip()
        else:
            result[pair.strip()] = ""
    return result


def format_as_json(data: Dict[str, Any], indent: int = 2) -> str:
    """Safely serialize dictionary data to formatted JSON string."""
    try:
        return json.dumps(data, indent=indent, default=str)
    except (TypeError, ValueError) as err:
        return f"{{\"error\": \"Failed to serialize: {str(err)}\"}}"
