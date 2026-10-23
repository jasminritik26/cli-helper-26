import re
import ipaddress

def is_valid_email(email: str) -> bool:
    """Validate email address format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def is_valid_ipv4(ip: str) -> bool:
    """Validate string is a valid IPv4 address."""
    try:
        return ipaddress.ip_address(ip).version == 4
    except ValueError:
        return False

def is_alphanumeric_with_underscores(value: str) -> bool:
    """Check if string contains only alphanumeric characters or underscores."""
    return bool(re.match(r'^[a-zA-Z0-9_]+$', value))

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Ensure integer falls within inclusive range."""
    return min_val <= value <= max_val

def is_non_empty_string(value: Any) -> bool:
    """Check if input is a non-empty string."""
    return isinstance(value, str) and len(value.strip()) > 0