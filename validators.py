import os
import re
from typing import Any, Dict

def validate_positive_integer(value: Any, field_name: str = "value") -> int:
    """Validate positive integer, handling None, non-int, <=0."""
    if value is None:
        raise ValueError(f"{field_name} cannot be None")
    try:
        num = int(value)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"{field_name} must be an integer, got {type(value).__name__}") from exc
    if num <= 0:
        raise ValueError(f"{field_name} must be positive, got {num}")
    return num

def validate_non_empty_string(value: Any, field_name: str = "value", max_len: int = 100) -> str:
    """Validate non-empty string within length, handling type and whitespace."""
    if value is None:
        raise ValueError(f"{field_name} cannot be None")
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    stripped = value.strip()
    if len(stripped) == 0:
        raise ValueError(f"{field_name} cannot be empty or only whitespace")
    if len(stripped) > max_len:
        raise ValueError(f"{field_name} exceeds maximum length of {max_len}")
    return stripped

def validate_file_path(path: Any, field_name: str = "path", must_exist: bool = False) -> str:
    """Validate and normalize path, optional existence check."""
    if not isinstance(path, str):
        raise TypeError(f"{field_name} must be a string")
    if not path or not path.strip():
        raise ValueError(f"{field_name} cannot be empty")
    normalized = os.path.normpath(path.strip())
    if must_exist and not os.path.exists(normalized):
        raise FileNotFoundError(f"{field_name} does not exist: {normalized}")
    return normalized

def validate_email_address(email: Any, field_name: str = "email") -> str:
    """Validate email format with regex after basic checks."""
    if email is None:
        raise ValueError(f"{field_name} cannot be None")
    if not isinstance(email, str):
        raise TypeError(f"{field_name} must be a string")
    stripped = email.strip()
    if not stripped:
        raise ValueError(f"{field_name} cannot be empty")
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, stripped):
        raise ValueError(f"{field_name} has invalid format")
    return stripped.lower()

def validate_cli_args(args: Dict[str, Any]) -> Dict[str, Any]:
    """Validate CLI args dict with field-specific validators."""
    if not isinstance(args, dict):
        raise TypeError("Arguments must be provided as a dictionary")
    if len(args) == 0:
        raise ValueError("No arguments provided")
    validated: Dict[str, Any] = {}
    for key, val in args.items():
        if key == "count":
            validated[key] = validate_positive_integer(val, key)
        elif key == "name":
            validated[key] = validate_non_empty_string(val, key, 50)
        elif key == "path":
            validated[key] = validate_file_path(val, key, must_exist=False)
        elif key == "email":
            validated[key] = validate_email_address(val, key)
        else:
            if val is None:
                raise ValueError(f"Value for {key} cannot be None")
            validated[key] = val
    return validated