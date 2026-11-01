import json
import shlex
from typing import Any, Dict, List, Optional


def safe_parse_json(raw_data: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Safely parse a JSON string into a dictionary, guarding against invalid types."""
    fallback = default if default is not None else {}
    if not isinstance(raw_data, str) or not raw_data.strip():
        return fallback

    try:
        parsed = json.loads(raw_data)
        return parsed if isinstance(parsed, dict) else fallback
    except (json.JSONDecodeError, TypeError, ValueError):
        return fallback


def truncate_text(text: str, max_length: int = 80, suffix: str = "...") -> str:
    """Truncate text to max_length safely handling negative lengths and non-string types."""
    if text is None:
        return ""
    
    str_text = str(text)
    if max_length <= 0:
        return ""
    
    if len(str_text) <= max_length:
        return str_text

    suffix_len = len(suffix)
    if max_length <= suffix_len:
        return str_text[:max_length]

    return str_text[: max_length - suffix_len] + suffix


def format_command_args(args: List[Any]) -> str:
    """Safely join shell arguments handling non-string elements and empty lists."""
    if not isinstance(args, (list, tuple)):
        return ""

    sanitized = []
    for arg in args:
        if arg is None:
            continue
        sanitized.append(shlex.quote(str(arg)))

    return " ".join(sanitized)
