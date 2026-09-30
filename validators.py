from typing import Any, Optional
import re

def validate_email(email: str) -> bool:
    """Validate email format using regex pattern."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def validate_integer_range(value: Any, min_val: int, max_val: int) -> bool:
    """Check if input is integer within inclusive bounds."""
    if not isinstance(value, int):
        return False
    return min_val <= value <= max_val

def validate_required_string(value: Optional[str]) -> bool:
    """Verify string is not empty or whitespace only."""
    return bool(value and value.strip())

def sanitize_input(value: str) -> str:
    """Remove leading/trailing whitespace and normalize string."""
    if not isinstance(value, str):
        return ""
    return value.strip().lower()

def validate_length(value: str, min_len: int, max_len: int = 255) -> bool:
    """Check string length constraints."""
    return min_len <= len(value) <= max_len