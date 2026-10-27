import os
import re
from typing import Any, Dict, List, Tuple


class ValidationError(Exception):
    """Raised when user input fails validation checks."""
    pass


def validate_command_args(args: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate argument dictionary passed from the main processing loop.
    
    Returns a tuple of (is_valid, list_of_error_messages).
    """
    errors = []

    # Validate output path if specified
    if "output" in args and args["output"]:
        output_dir = os.path.dirname(os.path.abspath(args["output"]))
        if not os.path.exists(output_dir):
            errors.append(f"Output directory does not exist: {output_dir}")

    # Validate timeout option if present
    if "timeout" in args and args["timeout"] is not None:
        try:
            val = float(args["timeout"])
            if val <= 0:
                errors.append("Timeout must be a positive number.")
        except (ValueError, TypeError):
            errors.append("Timeout must be a valid numeric value.")

    # Validate command name format
    if "command" in args:
        cmd = str(args["command"]).strip()
        if not cmd:
            errors.append("Command name cannot be empty.")
        elif not re.match(r"^[a-zA-Z0-9_\-]+$", cmd):
            errors.append("Command contains invalid characters.")

    return (len(errors) == 0, errors)


def sanitize_input(user_input: str) -> str:
    """Strip leading/trailing whitespace and remove non-printable characters."""
    if not isinstance(user_input, str):
        return ""
    cleaned = user_input.strip()
    return "".join(char for char in cleaned if char.isprintable())
