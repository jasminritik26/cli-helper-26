"""Validation and data sanitization utilities for CLI input handling."""

import re
from typing import Any, Dict, List, Optional, Tuple, Union


def validate_dict_keys(
    data: Dict[str, Any],
    required_keys: List[str],
    optional_keys: Optional[List[str]] = None,
) -> Tuple[bool, List[str]]:
    """Validate that a dictionary contains required keys and optional keys."""
    if not isinstance(data, dict):
        return False, ["Input must be a dictionary"]

    missing = [k for k in required_keys if k not in data]
    if missing:
        return False, [f"Missing required key: {k}" for k in missing]

    if optional_keys is not None:
        allowed = set(required_keys) | set(optional_keys)
        unknown = [k for k in data if k not in allowed]
        if unknown:
            return False, [f"Unknown key detected: {k}" for k in unknown]

    return True, []


def coerce_numeric(
    value: Any,
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
    default: Optional[Union[int, float]] = None,
) -> Optional[Union[int, float]]:
    """Attempt to convert value to int/float with optional bounds checking."""
    if value is None:
        return default

    try:
        num = float(value)
        if num.is_integer():
            num = int(num)
    except (ValueError, TypeError):
        return default

    if min_val is not None and num < min_val:
        return default
    if max_val is not None and num > max_val:
        return default

    return num


def sanitize_cli_arg(val: str, max_length: int = 255) -> str:
    """Strip control characters and truncate string to max length."""
    if not isinstance(val, str):
        val = str(val)

    cleaned = re.sub(r"[\x00-\x1f\x7f]", "", val.strip())
    return cleaned[:max_length]
