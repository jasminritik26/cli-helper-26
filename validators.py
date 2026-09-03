import os
import re
from typing import Union

def validate_port(port: Union[int, str]) -> int:
    """Validate that the given value is a valid TCP/UDP port number.

    Args:
        port: The port value to test, either as an integer or string.

    Returns:
        The parsed port number as an integer.

    Raises:
        ValueError: If the port is not an integer or is outside the range 1-65535.
    """
    try:
        parsed_port = int(port)
    except (TypeError, ValueError) as err:
        raise ValueError(f"Invalid port representation: {port}") from err

    if not (1 <= parsed_port <= 65535):
        raise ValueError(f"Port {parsed_port} is out of the valid range (1-65535)")

    return parsed_port

def validate_ip(ip_address: str) -> bool:
    """Determine whether the specified string is a valid IPv4 address.

    Args:
        ip_address: The string containing the candidate IP address.

    Returns:
        True if the string matches the IPv4 pattern, False otherwise.
    """
    if not isinstance(ip_address, str):
        return False
    
    ipv4_pattern = r"^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$"
    if not re.match(ipv4_pattern, ip_address):
        return False
    
    parts = ip_address.split('.')
    return all(0 <= int(part) <= 255 for part in parts)

def validate_existing_file(filepath: str) -> bool:
    """Check if the given path exists and points to a file.

    Args:
        filepath: The filesystem path to verify.

    Returns:
        True if the path is a file and exists, False otherwise.
    """
    if not filepath or not isinstance(filepath, str):
        return False
    return os.path.isfile(filepath)
