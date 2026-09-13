import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Validates email string format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def sanitize_input(data: Any) -> str:
    """Converts input to stripped string or returns empty."""
    if data is None:
        return ""
    return str(data).strip()

def is_non_empty(value: Any) -> bool:
    """Checks if value exists and is not whitespace."""
    if isinstance(value, str):
        return bool(value.strip())
    return value is not None

def ensure_list(data: Any) -> list:
    """Normalizes input to a flat list format."""
    if data is None:
        return []
    if isinstance(data, (list, tuple, set)):
        return list(data)
    return [data]

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Checks if integer is within inclusive boundaries."""
    return min_val <= value <= max_val