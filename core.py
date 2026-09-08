import subprocess
import sys
from typing import Optional, List

def format_color(text: str, color_code: str) -> str:
    """Wraps text in ANSI escape codes for terminal coloring."""
    return f"\u001b[{color_code}m{text}\u001b[0m"

def prompt_confirm(question: str, default: bool = True) -> bool:
    """Prompts the user for a yes/no confirmation."""
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    prompt = " [Y/n]: " if default else " [y/N]: "
    
    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower().strip()
        if choice == "" and default is not None:
            return default
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

def run_command(cmd: List[str]) -> Optional[str]:
    """Runs a system command and returns its stdout, or None on failure."""
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None