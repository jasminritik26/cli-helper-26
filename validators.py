import re
from pathlib import Path
from typing import Tuple, Union


def validate_port(port_input: Union[int, str]) -> int:
    """Validate and convert network port input.

    Args:
        port_input: Port number as integer or string.

    Returns:
        Validated integer port number.

    Raises:
        ValueError: If port is not a valid integer or out of range (1-65535).
    """
    try:
        port = int(port_input)
    except (TypeError, ValueError) as err:
        raise ValueError(f"Invalid port value: {port_input}") from err

    if not (1 <= port <= 65535):
        raise ValueError(f"Port number {port} out of range (1-65535)")
    return port


def validate_existing_path(path_str: str, must_be_dir: bool = False) -> Path:
    """Validate that a file or directory path exists.

    Args:
        path_str: Path string to validate.
        must_be_dir: If True, ensure path is a directory.

    Returns:
        Resolved Path object.

    Raises:
        FileNotFoundError: If the path does not exist.
        NotADirectoryError: If must_be_dir is True but path is a file.
    """
    path = Path(path_str).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path_str}")
    if must_be_dir and not path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {path_str}")
    return path


def validate_kv_pair(pair_str: str, delimiter: str = "=") -> Tuple[str, str]:
    """Parse and validate a key-value pair string.

    Args:
        pair_str: String formatted as 'key=value'.
        delimiter: Separator character, defaults to '='.

    Returns:
        Tuple containing (key, value).

    Raises:
        ValueError: If string cannot be split into exactly two parts.
    """
    parts = pair_str.split(delimiter, 1)
    if len(parts) != 2 or not parts[0].strip():
        raise ValueError(f"Invalid key-value pair format: '{pair_str}'")
    return parts[0].strip(), parts[1].strip()


def validate_identifier(name: str) -> str:
    """Check if string is a valid CLI identifier or option name.

    Args:
        name: Candidate string name.

    Returns:
        The validated name string.

    Raises:
        ValueError: If name contains invalid characters.
    """
    pattern = r"^[a-zA-Z0-9_-]+$"
    if not re.match(pattern, name):
        raise ValueError(
            f"Identifier '{name}' contains invalid characters"
        )
    return name
