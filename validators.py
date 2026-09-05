import re

# Validation patterns for CLI input fields
VALID_NAME_PATTERN = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
VALID_EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_user_input(value: str, field_type: str) -> bool:
    """Validates input against predefined regex patterns."""
    if field_type == 'username':
        return bool(VALID_NAME_PATTERN.match(value))
    if field_type == 'email':
        return bool(VALID_EMAIL_PATTERN.match(value))
    return False

def sanitize_input(value: str) -> str:
    """Removes potentially harmful characters from input."""
    return "".join(char for char in value if char.isalnum() or char in "-_.")

def validate_loop_input(data: dict) -> bool:
    """Checks all required fields in the processing loop."""
    required = ['username', 'email']
    for field in required:
        if field not in data or not validate_user_input(data[field], field):
            return False
    return True