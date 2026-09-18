import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """
    executes a function safely with error handling for edge cases
    returns the default value if an exception occurs during execution
    """
    try:
        if not callable(func):
            raise ValueError(f"expected callable, got {type(func).__name__}")
        return func(*args, **kwargs)
    except (TypeError, ValueError, AttributeError, KeyError) as e:
        logger.error(f"logic error in {func.__name__}: {str(e)}")
        return default
    except Exception as e:
        logger.critical(f"unexpected system error: {str(e)}")
        return default

def validate_input(data: Optional[Any], expected_type: type) -> bool:
    """
    verifies input against expected type with null safety
    returns false if input is missing or type mismatch
    """
    if data is None:
        return False
    try:
        return isinstance(data, expected_type)
    except Exception:
        return False

def format_response(payload: Any) -> str:
    """
    safely converts input to string for cli output
    """
    try:
        return str(payload) if payload is not None else ""
    except Exception:
        return "[serialization error]"