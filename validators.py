import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Verify if the provided string is a valid email format."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_non_empty_string(value: Any) -> bool:
    """Check if input is a string and not empty after stripping whitespace."""
    return isinstance(value, str) and len(value.strip()) > 0

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Confirm integer is within specified inclusive boundaries."""
    return isinstance(value, int) and min_val <= value <= max_val

def validate_url(url: str) -> bool:
    """Check if a string resembles a basic URL structure."""
    pattern = r'^https?:\/\/[\w\.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=]+$'
    return bool(re.match(pattern, url))

def sanitize_input(value: str) -> str:
    """Strip dangerous characters and whitespace from input strings."""
    if not isinstance(value, str):
        return ""
    return value.strip().replace("<", "").replace(">", "")