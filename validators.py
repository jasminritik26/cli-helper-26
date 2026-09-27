import re
from pathlib import Path
from typing import Union


def validate_command_name(name: str) -> bool:
    """Check if a CLI command name contains valid characters.

    Args:
        name: The command string to validate.

    Returns:
        True if valid alphanumeric with hyphens/underscores, False otherwise.
    """
    if not name or len(name) > 64:
        return False
    pattern = r"^[a-zA-Z0-9_-]+$"
    return bool(re.match(pattern, name))


def validate_filepath(
    path_str: Union[str, Path], must_exist: bool = False
) -> bool:
    """Validate whether a path string is well-formed and optionally exists.

    Args:
        path_str: String or Path object to validate.
        must_exist: If True, requires the target path to exist on disk.

    Returns:
        True if valid, False otherwise.
    """
    try:
        path = Path(path_str)
        if must_exist:
            return path.exists()
        return len(str(path)) > 0
    except (ValueError, TypeError):
        return False


def validate_port_number(
    port_value: Union[int, str], allow_privileged: bool = False
) -> bool:
    """Validate if a port number is within the acceptable network range.

    Args:
        port_value: Port number as integer or string.
        allow_privileged: If True, allows ports below 1024.

    Returns:
        True if port is valid, False otherwise.
    """
    try:
        port = int(port_value)
        min_port = 1 if allow_privileged else 1024
        return min_port <= port <= 65535
    except (ValueError, TypeError):
        return False


def validate_flag_name(flag: str) -> bool:
    """Verify that a CLI option flag follows standard naming formats.

    Args:
        flag: Flag string (e.g., '--verbose' or '-v').

    Returns:
        True if valid CLI flag syntax, False otherwise.
    """
    if not isinstance(flag, str):
        return False
    short_flag = bool(re.match(r"^-[a-zA-Z]$", flag))
    long_flag = bool(re.match(r"^--[a-zA-Z0-9-]+$", flag))
    return short_flag or long_flag
