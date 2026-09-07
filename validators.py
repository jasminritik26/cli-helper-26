import os

def validate_path(path: str) -> bool:
    """Checks if a path exists and is readable."""
    try:
        if not path or not isinstance(path, str):
            return False
        return os.path.exists(path) and os.access(path, os.R_OK)
    except (OSError, TypeError):
        return False

def validate_integer(value: any, min_val: int = 0, max_val: int = 100) -> int:
    """Safely parses input to integer within bounds."""
    try:
        parsed = int(value)
        if min_val <= parsed <= max_val:
            return parsed
        return min_val
    except (ValueError, TypeError):
        return min_val

def sanitize_input(user_input: str) -> str:
    """Removes potential shell injection characters."""
    if not user_input:
        return ""
    forbidden = [';', '&', '|', '>', '<', '`', '$']
    return ''.join(char for char in user_input if char not in forbidden).strip()