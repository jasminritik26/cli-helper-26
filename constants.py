import sys
from typing import Any, Dict

# Exit codes for error conditions including edge cases
EXIT_SUCCESS = 0
EXIT_INVALID_INPUT = 1
EXIT_MISSING_ARGUMENT = 2
EXIT_OUT_OF_RANGE = 3
EXIT_TYPE_MISMATCH = 4
EXIT_EMPTY_VALUE = 5
EXIT_UNKNOWN_ERROR = 99

# Templates for error messages
ERROR_TEMPLATES: Dict[int, str] = {
    EXIT_INVALID_INPUT: "Invalid input provided: {detail}",
    EXIT_MISSING_ARGUMENT: "Missing required argument: {detail}",
    EXIT_OUT_OF_RANGE: "Value is outside acceptable range: {detail}",
    EXIT_TYPE_MISMATCH: "Value has incorrect type: {detail}",
    EXIT_EMPTY_VALUE: "Value is empty or missing: {detail}",
}

FALLBACK_MESSAGE = "An unknown error occurred in the CLI helper."
MAX_DETAIL_LENGTH = 150

def get_error_message(code: int, detail: Any = None) -> str:
    """Return formatted error message handling various edge cases."""
    if code not in ERROR_TEMPLATES:
        return FALLBACK_MESSAGE
    template = ERROR_TEMPLATES[code]
    if detail is None:
        detail_str = "no details"
    else:
        try:
            detail_str = str(detail)
        except Exception:
            detail_str = "unrepresentable detail"
    if len(detail_str) > MAX_DETAIL_LENGTH:
        detail_str = detail_str[:MAX_DETAIL_LENGTH] + "..."
    if not detail_str or detail_str.isspace():
        detail_str = "no details"
    try:
        return template.format(detail=detail_str)
    except Exception:
        return template + " (detail: " + detail_str + ")"

def handle_error(code: int, detail: Any = None, exit_on_error: bool = True) -> None:
    """Print error to stderr and optionally exit, handling bad inputs."""
    if not isinstance(code, int):
        code = EXIT_UNKNOWN_ERROR
        detail = "Error code must be integer"
    message = get_error_message(code, detail)
    print("CLI-ERROR[" + str(code) + "]: " + message, file=sys.stderr)
    if exit_on_error:
        exit_code = code if 0 <= code <= 255 else EXIT_UNKNOWN_ERROR
        sys.exit(exit_code)

def process_input_safely(value: Any, name: str = "input") -> None:
    """Validate input for common edge cases like None, empty, negative, type errors."""
    if value is None:
        handle_error(EXIT_INVALID_INPUT, name + " cannot be None", exit_on_error=False)
        return
    if isinstance(value, str):
        stripped = value.strip()
        if len(stripped) == 0:
            handle_error(EXIT_EMPTY_VALUE, name, exit_on_error=False)
        elif len(stripped) > 1000:
            handle_error(EXIT_OUT_OF_RANGE, name + " too long", exit_on_error=False)
    elif isinstance(value, (int, float)):
        if value < 0:
            handle_error(EXIT_OUT_OF_RANGE, name + " is negative", exit_on_error=False)
    elif not isinstance(value, bool):
        handle_error(EXIT_TYPE_MISMATCH, name + " has invalid type", exit_on_error=False)

# Constants for error related limits
MAX_RETRIES = 5
TIMEOUT_SECONDS = 30