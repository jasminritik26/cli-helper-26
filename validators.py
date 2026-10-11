import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_non_empty_string(value: Any, field_name: str) -> str:
    """Ensures value is a non-empty, stripped string."""
    if not isinstance(value, str):
        raise ValidationError(f"{field_name} must be a string, got {type(value).__name__}")
    
    sanitized = value.strip()
    if not sanitized:
        raise ValidationError(f"{field_name} cannot be empty or whitespace")
    
    return sanitized

def validate_integer_range(value: Any, min_val: int, max_val: int) -> int:
    """Ensures value is within an inclusive integer range."""
    try:
        val_int = int(value)
    except (ValueError, TypeError):
        raise ValidationError(f"Expected integer, received '{value}'")
    
    if not (min_val <= val_int <= max_val):
        raise ValidationError(f"Value {val_int} out of bounds [{min_val}, {max_val}]")
    
    return val_int

def safe_process_input(func, *args, **kwargs) -> Optional[Any]:
    """Wrapper to handle validation errors gracefully."""
    try:
        return func(*args, **kwargs)
    except ValidationError as e:
        logger.error(f"Validation failed: {e}")
        return None
    except Exception as e:
        logger.critical(f"Unexpected system error: {e}", exc_info=True)
        return None