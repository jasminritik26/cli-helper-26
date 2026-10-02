from typing import Any, Optional
import re

def validate_email(email: str) -> bool:
    """
    Check if the provided string follows standard email format.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_port(port: Any) -> bool:
    """
    Verify that the input is a valid network port number.

    Args:
        port (Any): The port identifier to check.

    Returns:
        bool: True if within range [1, 65535], False otherwise.
    """
    try:
        port_int = int(port)
        return 1 <= port_int <= 65535
    except (ValueError, TypeError):
        return False

def sanitize_input(value: Optional[str]) -> str:
    """
    Remove leading and trailing whitespace from input.

    Args:
        value (Optional[str]): The raw input string.

    Returns:
        str: Sanitized string or empty if input was None.
    """
    if value is None:
        return ""
    return str(value).strip()