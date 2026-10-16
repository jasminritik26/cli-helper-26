"""Utility functions for CLI output formatting, string manipulation, and system interaction."""

import shutil
import sys
from typing import Any, List


def format_table(headers: List[str], rows: List[List[Any]], padding: int = 2) -> str:
    """Format tabular data into a plain text aligned table."""
    if not rows:
        return ""

    all_data = [headers] + [[str(cell) for cell in row] for row in rows]
    col_widths = [max(len(str(row[i])) for row in all_data) for i in range(len(headers))]

    formatted_rows = []
    for row in all_data:
        formatted_cells = [str(cell).ljust(col_widths[i] + padding) for i, cell in enumerate(row)]
        formatted_rows.append("".join(formatted_cells).rstrip())

    separator = "".join(["-" * width + " " * padding for width in col_widths]).rstrip()
    formatted_rows.insert(1, separator)

    return "\
".join(formatted_rows)


def get_terminal_width(default: int = 80) -> int:
    """Retrieve current terminal width safely with fallback."""
    try:
        return shutil.get_terminal_size((default, 24)).columns
    except (AttributeError, ValueError):
        return default


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length including suffix if exceeded."""
    if len(text) <= max_length:
        return text

    cutoff = max_length - len(suffix)
    return text[:cutoff] + suffix if cutoff > 0 else text[:max_length]


def confirm_prompt(message: str, default: bool = False) -> bool:
    """Prompt user for yes/no confirmation in terminal."""
    choices = " [Y/n]: " if default else " [y/N]: "
    sys.stdout.write(message + choices)
    sys.stdout.flush()

    response = sys.stdin.readline().strip().lower()
    if not response:
        return default
    return response in ("y", "yes")
