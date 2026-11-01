import sys
import shutil
from typing import Optional


def format_bytes(size: float) -> str:
    """Format a byte count into a human-readable string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if abs(size) < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} PB"


def truncate_text(text: str, max_length: int = 50, ellipsis: str = "...") -> str:
    """Truncate text to a maximum length with an ellipsis."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(ellipsis)] + ellipsis


def prompt_confirm(message: str, default: bool = True) -> bool:
    """Prompt the user for a boolean yes/no response in the CLI."""
    suffix = " [Y/n]" if default else " [y/N]"
    sys.stdout.write(f"{message}{suffix}: ")
    sys.stdout.flush()

    response = sys.stdin.readline().strip().lower()
    if not response:
        return default
    return response in ("y", "yes")


def get_terminal_width(default: int = 80) -> int:
    """Get the current terminal width in characters."""
    try:
        columns, _ = shutil.get_terminal_size(fallback=(default, 24))
        return columns
    except Exception:
        return default


def print_divider(char: str = "-", max_width: Optional[int] = None) -> None:
    """Print a horizontal divider rule across the terminal."""
    width = get_terminal_width()
    if max_width and width > max_width:
        width = max_width
    print(char * width)
