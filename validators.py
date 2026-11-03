import os
from pathlib import Path
from typing import Tuple, Union


def validate_port(value: Union[int, str]) -> int:
    """Validate that a given value is a valid network port number.

    Args:
        value: Port number as an integer or string.

    Returns:
        The port number as an integer.

    Raises:
        ValueError: If value cannot be converted or is out of range (1-65535).
    """
    try:
        port = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Port must be an integer, got '{value}'")

    if not (1 <= port <= 65535):
        raise ValueError(f"Port must be between 1 and 65535, got {port}")
    return port


def validate_filepath(
    path: Union[str, Path],
    must_exist: bool = False,
    writable: bool = False,
) -> Path:
    """Validate and resolve a file system path.

    Args:
        path: String or Path object representing a file path.
        must_exist: If True, ensures the path exists on disk.
        writable: If True, checks whether the target location is writable.

    Returns:
        Resolved Path object.

    Raises:
        FileNotFoundError: If must_exist is True and path does not exist.
        PermissionError: If writable is True and directory is not writable.
    """
    resolved_path = Path(path).expanduser().resolve()

    if must_exist and not resolved_path.exists():
        raise FileNotFoundError(f"Path does not exist: {resolved_path}")

    if writable:
        target_dir = resolved_path if resolved_path.is_dir() else resolved_path.parent
        if target_dir.exists() and not os.access(target_dir, os.W_OK):
            raise PermissionError(f"Directory is not writable: {target_dir}")

    return resolved_path


def validate_key_value(pair_str: str, delimiter: str = "=") -> Tuple[str, str]:
    """Parse and validate a key-value pair string.

    Args:
        pair_str: Input string containing key and value separated by delimiter.
        delimiter: Separator character (defaults to '=').

    Returns:
        Tuple of (key, value) stripped of leading/trailing whitespace.

    Raises:
        ValueError: If delimiter is missing or key is empty.
    """
    if delimiter not in pair_str:
        raise ValueError(f"Expected '{delimiter}' in key-value pair '{pair_str}'")

    key, value = pair_str.split(delimiter, 1)
    key, value = key.strip(), value.strip()

    if not key:
        raise ValueError(f"Key cannot be empty in pair '{pair_str}'")

    return key, value
