import json
from typing import Any, Dict, List, Optional


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary for standard key-value output."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict) and value:
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def sanitize_cli_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Clean dictionary values into safe strings for CLI output or logging."""
    cleaned: Dict[str, Any] = {}
    for key, value in data.items():
        if value is None:
            continue
        if isinstance(value, (dict, list, tuple)):
            cleaned[key] = json.dumps(value)
        else:
            cleaned[key] = str(value)
    return cleaned


def filter_by_keys(
    data: Dict[str, Any],
    include: Optional[List[str]] = None,
    exclude: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Filter dictionary key-value pairs based on inclusion and exclusion rules."""
    result = data.copy()
    if include is not None:
        result = {k: v for k, v in result.items() if k in include}
    if exclude is not None:
        result = {k: v for k, v in result.items() if k not in exclude}
    return result
