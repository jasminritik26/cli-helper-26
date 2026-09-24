"""Terminal formatting and CLI input helper functions."""

import shutil
import sys
from typing import List, Optional, Tuple


def get_terminal_size(default: Tuple[int, int] = (80, 24)) -> Tuple[int, int]:
    """Return terminal width and height safely."""
    try:
        columns, lines = shutil.get_terminal_size(fallback=default)
        return columns, lines
    except (AttributeError, ValueError):
        return default


def format_header(text: str, char: str = "=", width: Optional[int] = None) -> str:
    """Format a text title centered inside decorative border lines."""
    if width is None:
        width, _ = get_terminal_size()
    border = char * max(width, len(text))
    return f"{border}\n{text.center(width)}\n{border}"


def truncate_text(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """Truncate text to max_length if it exceeds the limit."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def parse_kv_args(args: List[str]) -> dict:
    """Parse key=value string pairs from command line arguments."""
    result = {}
    for arg in args:
        if "=" in arg:
            key, value = arg.split("=", 1)
            result[key.strip()] = value.strip()
    return result


def confirm_action(prompt: str, default: bool = False) -> bool:
    """Prompt the user for a yes/no confirmation in CLI."""
    suffix = " [Y/n]: " if default else " [y/N]: "
    try:
        response = input(f"{prompt}{suffix}").strip().lower()
        if not response:
            return default
        return response in ("y", "yes")
    except (KeyboardInterrupt, EOFError):
        sys.stdout.write("\n")
        return False
