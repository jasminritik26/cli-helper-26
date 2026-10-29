import sys
from typing import Any, Dict


def format_bytes(size_in_bytes: int) -> str:
    """Format a byte count into a human-readable string."""
    if size_in_bytes < 0:
        raise ValueError("Size cannot be negative")

    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_in_bytes)
    unit_index = 0

    while size >= 1024.0 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"


def truncate_text(text: str, max_length: int = 40, suffix: str = "...") -> str:
    """Truncate text to a maximum length with an optional suffix."""
    if len(text) <= max_length:
        return text
    if max_length <= len(suffix):
        return suffix[:max_length]
    return text[: max_length - len(suffix)] + suffix


def confirm_prompt(message: str, default: bool = False) -> bool:
    """Prompt the user for a yes/no response in the terminal."""
    suffix = " [Y/n]: " if default else " [y/N]: "
    try:
        response = input(f"{message}{suffix}").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print()
        return False

    if not response:
        return default
    return response in ("y", "yes")


def print_kv_table(data: Dict[str, Any], key_width: int = 20) -> None:
    """Print a simple key-value dictionary as a formatted table."""
    for key, value in data.items():
        padded_key = str(key).ljust(key_width)
        print(f"{padded_key} : {value}")
