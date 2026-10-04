import re
import os

def validate_email(email: str) -> bool:
    """Verify email format using standard regex pattern."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_path_exists(path: str) -> bool:
    """Check if the provided filesystem path is valid and exists."""
    return os.path.exists(path)

def validate_integer_range(value: any, min_val: int, max_val: int) -> bool:
    """Check if input is integer within specified inclusive range."""
    try:
        val = int(value)
        return min_val <= val <= max_val
    except (ValueError, TypeError):
        return False

def validate_alphanumeric(text: str) -> bool:
    """Ensure string contains only letters and numbers."""
    return text.isalnum()

def validate_non_empty(text: str) -> bool:
    """Ensure string is not empty after stripping whitespace."""
    return bool(text and text.strip())