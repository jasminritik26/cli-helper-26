import os
import shutil
import sys
from typing import Union


def format_bytes(size_in_bytes: Union[int, float]) -> str:
    """Format a byte count into a human-readable string (e.g., KiB, MiB)."""
    if size_in_bytes < 0:
        raise ValueError("Size cannot be negative")

    for unit in ["B", "KiB", "MiB", "GiB", "TiB"]:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} PiB"


def confirm_action(prompt: str, default: bool = True) -> bool:
    """Prompt the user for a yes/no confirmation in the terminal."""
    valid_responses = {"y": True, "yes": True, "n": False, "no": False}
    suffix = " [Y/n]" if default else " [y/N]"

    while True:
        sys.stdout.write(f"{prompt}{suffix}: ")
        sys.stdout.flush()
        choice = sys.stdin.readline().strip().lower()

        if not choice:
            return default

        if choice in valid_responses:
            return valid_responses[choice]

        sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate a string to a maximum length, appending a suffix if truncated."""
    if len(text) <= max_length:
        return text

    adjusted_len = max_length - len(suffix)
    if adjusted_len <= 0:
        return suffix[:max_length]

    return text[:adjusted_len] + suffix


def get_terminal_width(fallback: int = 80) -> int:
    """Retrieve the current terminal width, falling back to a default value."""
    try:
        columns, _ = shutil.get_terminal_size(fallback=(fallback, 24))
        return columns
    except (AttributeError, ValueError):
        # Fallback for environments without standard terminal access
        return int(os.environ.get("COLUMNS", fallback))
