import collections
from typing import Dict, Any

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Recursively flattens a nested dictionary into a single-level dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def unflatten_dict(d: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    """
    Reconstructs a nested dictionary from a flattened dictionary.
    """
    result = {}
    for key, value in d.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current or not isinstance(current[part], dict):
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result

def remove_empty_values(d: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively removes key-value pairs where the value is empty or None.
    """
    clean = {}
    for k, v in d.items():
        if v in (None, "", [], {}):
            continue
        if isinstance(v, dict):
            nested = remove_empty_values(v)
            if nested:
                clean[k] = nested
        else:
            clean[k] = v
    return clean
