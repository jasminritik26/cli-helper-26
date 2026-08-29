"""Core helper functions for CLI operations."""

import os
import time
from typing import Any, Callable, Dict, List, Optional

def get_env(name: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieve environment variable with optional default."""
    return os.getenv(name, default)

def confirm_action(prompt: str, default: bool = False) -> bool:
    """Ask for user confirmation with default option."""
    options = "Y/n" if default else "y/N"
    try:
        response = input(f"{prompt} [{options}]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return default
    if not response:
        return default
    return response in ('y', 'yes')

def format_table(data: List[Dict[str, Any]], headers: Optional[List[str]] = None) -> str:
    """Return a formatted table from list of dictionaries."""
    if not data:
        return "No data to display."
    if headers is None:
        headers = list(data[0].keys())
    # Determine column widths
    widths: Dict[str, int] = {}
    for key in headers:
        max_len = len(str(key))
        for row in data:
            val = str(row.get(key, ''))
            if len(val) > max_len:
                max_len = len(val)
        widths[key] = max_len
    # Build the table
    header_row = " | ".join(str(h).ljust(widths[h]) for h in headers)
    separator = "-+-".join("-" * widths[h] for h in headers)
    table_rows = []
    for row in data:
        row_line = " | ".join(str(row.get(h, '')).ljust(widths[h]) for h in headers)
        table_rows.append(row_line)
    return "\n".join([header_row, separator] + table_rows)

def retry_operation(func: Callable[[], Any], max_retries: int = 3, delay: float = 1.0) -> Any:
    """Execute function with retry on exception."""
    last_exc = None
    for i in range(max_retries):
        try:
            return func()
        except Exception as e:
            last_exc = e
            if i < max_retries - 1:
                time.sleep(delay)
    if last_exc:
        raise last_exc
    return None

def get_choice(prompt: str, options: List[str]) -> Optional[str]:
    """Prompt user to select from list of options."""
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    try:
        choice = int(input("Enter choice: ").strip())
        if 1 <= choice <= len(options):
            return options[choice - 1]
    except (ValueError, EOFError, KeyboardInterrupt):
        pass
    return None