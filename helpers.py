from typing import List, Optional, Any
import os

def format_output(data: List[str], prefix: str = '>>') -> str:
    """Formats a list of strings into a standard console output string."""
    return "\n".join([f"{prefix} {item}" for item in data])

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with a fallback default value."""
    return os.environ.get(key, default or "")

def clean_input(raw_input: Any) -> str:
    """Converts input to a stripped string safe for CLI processing."""
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)
    return raw_input.strip()

def validate_path(path: str) -> bool:
    """Checks if the provided path string exists on the filesystem."""
    return os.path.exists(path)

def summarize_payload(payload: dict) -> str:
    """Creates a compact summary string for dictionary based payloads."""
    keys = ", ".join(payload.keys())
    return f"Payload containing: {keys}"