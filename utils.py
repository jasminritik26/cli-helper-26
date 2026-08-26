import sys
import os
from typing import Any, Dict, List, Optional

def format_output(data: Dict[str, Any], indent: int = 2) -> str:
    """Format a dictionary into a readable string representation."""
    import json
    try:
        return json.dumps(data, indent=indent, sort_keys=True)
    except (TypeError, ValueError) as e:
        return f"Error formatting output: {e}"

def safe_file_read(filepath: str) -> Optional[str]:
    """Safely read text from a file, returning None if an error occurs."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError:
        return None

def parse_key_value_args(args: List[str]) -> Dict[str, str]:
    """Parse a list of 'key=value' command line arguments into a dictionary."""
    result = {}
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            result[key.strip()] = value.strip()
    return result

def print_error_and_exit(message: str, code: int = 1) -> None:
    """Print an error message to stderr and exit the program."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(code)
