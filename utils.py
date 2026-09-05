from typing import List, Optional, Dict, Any
import os

def format_path(path: str) -> str:
    """Normalize and expand user path for consistent file access."""
    return os.path.expanduser(os.path.normpath(path))

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller segments of a specified size."""
    if size <= 0:
        return [items]
    return [items[i:i + size] for i in range(0, len(items), size)]

def merge_configs(base: Dict[str, Any], override: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Update base dictionary with non-null values from override."""
    config = base.copy()
    if override:
        for key, value in override.items():
            if value is not None:
                config[key] = value
    return config

def validate_name(name: str) -> bool:
    """Check if a string contains only alphanumeric characters."""
    return bool(name and name.isalnum())

def get_environment_info(key: str, default: str = "unknown") -> str:
    """Retrieve system environment variables with a fallback value."""
    return os.environ.get(key, default)