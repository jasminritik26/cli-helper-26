"""Common utility helpers for CLI operations."""

import sys
from typing import Dict, List, Optional


def format_bytes(size_in_bytes: int) -> str:
    """Convert a byte count into a human-readable string format."""
    if size_in_bytes < 0:
        raise ValueError("Size cannot be negative")
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_in_bytes)
    for unit in units:
        if size < 1024.0 or unit == units[-1]:
            return f"{size:.2f} {unit}" if unit != "B" else f"{int(size)} B"
        size /= 1024.0
    return f"{size:.2f} TB"


def confirm_prompt(prompt_text: str, default_yes: bool = True) -> bool:
    """Ask user a yes/no question via standard input and return boolean result."""
    suffix = " [Y/n]: " if default_yes else " [y/N]: "
    sys.stdout.write(prompt_text + suffix)
    sys.stdout.flush()

    response = sys.stdin.readline().strip().lower()
    if not response:
        return default_yes
    return response in ("y", "yes")


def parse_key_value_pairs(raw_items: List[str]) -> Dict[str, str]:
    """Parse a list of key=value CLI arguments into a dictionary."""
    parsed = {}
    for item in raw_items:
        if "=" not in item:
            continue
        key, value = item.split("=", 1)
        key = key.strip()
        if key:
            parsed[key] = value.strip()
    return parsed


def truncate_string(text: str, max_len: int = 40, suffix: str = "...") -> str:
    """Truncate text to a maximum length and append a suffix if needed."""
    if len(text) <= max_len:
        return text
    return text[: max_len - len(suffix)] + suffix
