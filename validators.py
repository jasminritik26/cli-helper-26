"""Input validation utilities with defensive edge-case error handling."""

import json
import os
import shutil
from typing import List, Optional, Union


class ValidationError(Exception):
    """Raised when CLI input fails validation checks."""
    pass


def validate_file_path(path: Union[str, os.PathLike], must_exist: bool = True, writable: bool = False) -> str:
    """Validate and resolve a file path, checking existence and access permissions."""
    if not path or not str(path).strip():
        raise ValidationError("Provided path cannot be empty or whitespaces only.")

    resolved_path = os.path.abspath(os.path.expanduser(str(path)))

    if must_exist and not os.path.exists(resolved_path):
        raise ValidationError(f"Target path does not exist: {resolved_path}")

    if must_exist and os.path.isdir(resolved_path):
        raise ValidationError(f"Expected a file path, but got a directory: {resolved_path}")

    if writable:
        target_dir = os.path.dirname(resolved_path) if not os.path.exists(resolved_path) else resolved_path
        if not os.access(target_dir, os.W_OK):
            raise ValidationError(f"Permission denied: cannot write to path {resolved_path}")

    return resolved_path


def validate_json_payload(raw_data: Optional[str]) -> dict:
    """Parse and validate JSON input, handling edge cases like empty strings and non-dict roots."""
    if raw_data is None:
        raise ValidationError("Payload cannot be None.")

    trimmed = raw_data.strip()
    if not trimmed:
        raise ValidationError("Empty payload received.")

    try:
        parsed = json.loads(trimmed)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON string provided: {exc.msg} at line {exc.lineno}") from exc

    if not isinstance(parsed, dict):
        raise ValidationError(f"JSON payload must be a key-value object, got {type(parsed).__name__}.")

    return parsed


def validate_executable_command(command: Union[str, List[str]]) -> List[str]:
    """Validate shell commands or binary names before execution."""
    if isinstance(command, str):
        parts = command.strip().split()
    elif isinstance(command, list):
        parts = [str(arg).strip() for arg in command if str(arg).strip()]
    else:
        raise ValidationError("Command must be a string or list of argument strings.")

    if not parts:
        raise ValidationError("Command cannot be empty.")

    binary = parts[0]
    if not shutil.which(binary):
        raise ValidationError(f"Executable binary '{binary}' not found in system PATH.")

    return parts
