"""General utility helpers for formatting and interactive CLI operations."""

from typing import Dict, List, Optional


def format_header(title: str, width: int = 60, char: str = "=") -> str:
    """Format a centered title header enclosed in border characters.

    Args:
        title: The string title to format inside the header.
        width: Total width of the header line in characters.
        char: Single character used to construct the border line.

    Returns:
        A formatted multi-line header string.
    """
    border = char * width
    centered_title = title.center(width - 4)
    return f"{border}\n{char} {centered_title} {char}\n{border}"


def confirm_action(prompt: str, default: bool = False) -> bool:
    """Prompt the user for a boolean yes/no confirmation.

    Args:
        prompt: The message displayed to the user.
        default: Default return value if user presses Enter without typing.

    Returns:
        True if the user accepted, False otherwise.
    """
    options = "[Y/n]" if default else "[y/N]"
    response = input(f"{prompt} {options}: ").strip().lower()

    if not response:
        return default
    return response in ("y", "yes", "true", "1")


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to a maximum length and attach a suffix if trimmed.

    Args:
        text: Target text string to truncate.
        max_length: Maximum allowed character length including suffix.
        suffix: Indicator appended to truncated strings.

    Returns:
        The original or truncated text string.
    """
    if len(text) <= max_length:
        return text

    trim_len = max(0, max_length - len(suffix))
    return text[:trim_len] + suffix


def parse_kv_pairs(args: List[str]) -> Dict[str, str]:
    """Parse a list of key=value command-line strings into a dictionary.

    Args:
        args: List of raw arguments in 'key=value' format.

    Returns:
        Dictionary mapping string keys to string values.
    """
    result: Dict[str, str] = {}
    for arg in args:
        if "=" in arg:
            key, val = arg.split("=", 1)
            result[key.strip()] = val.strip()
    return result
