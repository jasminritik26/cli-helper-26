import os
import subprocess
import sys
from typing import Tuple


def format_text(text: str, color: str) -> str:
    """Formats text with ANSI color codes for terminal output."""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "bold": "\033[1m",
        "reset": "\033[0m",
    }
    # Disable colors if terminal output is redirected or not a tty
    if not sys.stdout.isatty() or os.getenv("NO_COLOR"):
        return text

    color_code = colors.get(color.lower(), "")
    reset_code = colors["reset"] if color_code else ""
    return f"{color_code}{text}{reset_code}"


def confirm_action(prompt: str, default: bool = False) -> bool:
    """Prompts the user for a yes/no confirmation in the terminal."""
    valid = {"yes": True, "y": True, "no": False, "n": False}
    suffix = " [Y/n]" if default else " [y/N]"

    while True:
        sys.stdout.write(f"{prompt}{suffix}: ")
        try:
            choice = input().lower().strip()
        except (KeyboardInterrupt, EOFError):
            sys.stdout.write("\n")
            return False

        if not choice:
            return default
        if choice in valid:
            return valid[choice]
        sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def run_command(cmd: str) -> Tuple[int, str, str]:
    """Executes a system command and returns code, stdout, and stderr."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return -1, "", str(e)
