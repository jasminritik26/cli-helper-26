import re
import sys


def format_bytes(size: int) -> str:
    """Convert byte counts into a human-readable string representation."""
    if size < 0:
        raise ValueError("Size cannot be negative")
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    value = float(size)
    for unit in units:
        if value < 1024.0 or unit == units[-1]:
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024.0
    return f"{value:.1f} PB"


def truncate_string(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """Truncate text to a maximum length and append suffix if needed."""
    if len(text) <= max_length:
        return text
    if max_length <= len(suffix):
        return suffix[:max_length]
    return text[: max_length - len(suffix)] + suffix


def sanitize_filename(name: str, replacement: str = "_") -> str:
    """Remove unsafe characters from a string to create a safe filename."""
    clean_name = re.sub(r'[\\/*?:"<>|]', replacement, name)
    clean_name = clean_name.strip(". ")
    return clean_name or "unnamed_file"


def prompt_confirm(message: str, default: bool = True) -> bool:
    """Ask a yes/no question via standard input and return boolean."""
    hint = "[Y/n]" if default else "[y/N]"
    sys.stdout.write(f"{message} {hint} ")
    sys.stdout.flush()
    response = sys.stdin.readline().strip().lower()

    if not response:
        return default
    return response in ("y", "yes")