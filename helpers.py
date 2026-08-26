"""Utility helper functions for CLI operations."""

from typing import Any, Dict, List, Optional


def format_output(data: Dict[str, Any], indent: int = 2) -> str:
    """Format dictionary data into a readable string representation.

    Args:
        data: The dictionary to format.
        indent: The number of spaces for indentation.

    Returns:
        A formatted string representation of the data.
    """
    import json
    try:
        return json.dumps(data, indent=indent)
    except (TypeError, ValueError) as e:
        return f"Error formatting output: {e}"


def parse_arguments(raw_args: List[str]) -> Dict[str, str]:
    """Parse raw command line arguments into a key-value mapping.

    Args:
        raw_args: A list of raw argument strings.

    Returns:
        A dictionary containing parsed key-value pairs.
    """
    parsed: Dict[str, str] = {}
    current_key: Optional[str] = None

    for arg in raw_args:
        if arg.startswith("--"):
            current_key = arg[2:]
            parsed[current_key] = ""
        elif current_key is not None:
            parsed[current_key] = arg
            current_key = None

    return parsed


def truncate_string(text: str, max_length: int = 50) -> str:
    """Truncate a string to a maximum length with an ellipsis.

    Args:
        text: The string to truncate.
        max_length: Maximum allowed length before truncation.

    Returns:
        The truncated string.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
