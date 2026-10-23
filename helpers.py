"""General helper utilities for CLI operations."""

import sys
from typing import Dict, List


def format_bytes(size_in_bytes: int) -> str:
    """Format byte sizes into human-readable strings."""
    if size_in_bytes < 0:
        raise ValueError("Size cannot be negative")
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_in_bytes)
    for unit in units:
        if size < 1024.0 or unit == units[-1]:
            return f"{size:.2f} {unit}" if unit != "B" else f"{int(size)} B"
        size /= 1024.0
    return f"{size:.2f} PB"


def truncate_text(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """Truncate text to a maximum length with optional suffix."""
    if len(text) <= max_length:
        return text
    if max_length <= len(suffix):
        return text[:max_length]
    return text[: max_length - len(suffix)] + suffix


def parse_key_value(items: List[str], delimiter: str = "=") -> Dict[str, str]:
    """Parse a list of key-value pair strings into a dictionary."""
    result: Dict[str, str] = {}
    for item in items:
        if delimiter in item:
            key, value = item.split(delimiter, 1)
            result[key.strip()] = value.strip()
        else:
            result[item.strip()] = ""
    return result


def confirm_prompt(message: str, default: bool = False) -> bool:
    """Display a confirmation prompt and return boolean response."""
    suffix = " [Y/n]: " if default else " [y/N]: "
    try:
        response = input(f"{message}{suffix}").strip().lower()
        if not response:
            return default
        return response in ("y", "yes", "true", "1")
    except (KeyboardInterrupt, EOFError):
        sys.stdout.write("\n")
        return False
