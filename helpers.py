import os
import sys
import time
from contextlib import contextmanager
from typing import Generator

def clean_screen() -> None:
    """Clears the terminal screen in a cross-platform manner."""
    os.system('cls' if os.name == 'nt' else 'clear')

def confirm_action(prompt: str, default: bool = False) -> bool:
    """Prompts the user for a yes/no confirmation.

    Returns True for yes, False for no.
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    suffix = " [Y/n]" if default else " [y/N]"

    while True:
        sys.stdout.write(f"{prompt}{suffix}: ")
        choice = input().lower().strip()
        if not choice:
            return default
        if choice in valid:
            return valid[choice]
        sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

@contextmanager
def execution_timer(operation_name: str = "Operation") -> Generator[None, None, None]:
    """Context manager to measure and print the execution time of a block."""
    start_time = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start_time
        print(f"[{operation_name}] Completed in {elapsed:.4f} seconds.")

def highlight_text(text: str, color_code: str = "32") -> str:
    """Wraps text in ANSI escape codes for basic terminal coloring.

    32 = Green, 31 = Red, 33 = Yellow, 34 = Blue, 36 = Cyan.
    """
    if sys.stdout.isatty():
        esc = chr(27)
        return f"{esc}[{color_code}m{text}{esc}[0m"
    return text