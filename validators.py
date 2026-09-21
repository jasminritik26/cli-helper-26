import os
from pathlib import Path
from typing import List, Union


def validate_file_path(path_str: str, must_exist: bool = True) -> Path:
    """Validate and convert a string representation of a file path into a Path object.

    Args:
        path_str: The string path to validate.
        must_exist: Flag indicating if the file must currently exist.

    Returns:
        A resolved Path object.

    Raises:
        ValueError: If the path string is empty.
        FileNotFoundError: If must_exist is True and the file does not exist.
    """
    if not path_str or not path_str.strip():
        raise ValueError("Path string cannot be empty.")

    path = Path(path_str).expanduser().resolve()

    if must_exist and not path.exists():
        raise FileNotFoundError(f"Target path does not exist: {path}")

    return path


def validate_port_number(port: Union[int, str], allow_reserved: bool = False) -> int:
    """Validate if a given value is a valid TCP/UDP port number.

    Args:
        port: The port number as an integer or string.
        allow_reserved: If False, ports under 1024 are disallowed.

    Returns:
        The validated port number as an integer.

    Raises:
        ValueError: If port cannot be converted to int or is out of range.
    """
    try:
        port_num = int(port)
    except (ValueError, TypeError):
        raise ValueError(f"Port must be an integer, got: {port}")

    min_port = 1024 if not allow_reserved else 1
    if not (min_port <= port_num <= 65535):
        raise ValueError(f"Port {port_num} out of valid range ({min_port}-65535).")

    return port_num


def validate_choice(value: str, choices: List[str], case_sensitive: bool = False) -> str:
    """Validate that a string option is within a predefined list of allowed choices.

    Args:
        value: The input value to check.
        choices: List of acceptable string options.
        case_sensitive: Whether matching should respect letter casing.

    Returns:
        The normalized matched choice from the list.

    Raises:
        ValueError: If value is not found in choices.
    """
    if not case_sensitive:
        normalized_value = value.lower()
        lookup = {c.lower(): c for c in choices}
        if normalized_value in lookup:
            return lookup[normalized_value]
    elif value in choices:
        return value

    allowed = ", ".join(choices)
    raise ValueError(f"Invalid choice '{value}'. Must be one of: {allowed}")
