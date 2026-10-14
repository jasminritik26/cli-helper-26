class CLIError(Exception):
    """Base exception for cli-helper-26."""
    pass

class ConfigurationError(CLIError):
    """Raised when configuration files are missing or malformed."""
    pass

class ValidationError(CLIError):
    """Raised when input parameters fail validation."""
    pass

class ProcessingError(CLIError):
    """Raised when the core logic encounters an internal state failure."""
    pass

def handle_exception(e: Exception) -> None:
    """Standardized logging and exit handling for library exceptions."""
    if isinstance(e, CLIError):
        print(f"[ERROR] {e.__class__.__name__}: {str(e)}")
    else:
        print(f"[CRITICAL] Unexpected error: {str(e)}")

def safe_execute(func, *args, **kwargs):
    """Decorator pattern helper for wrapped execution blocks."""
    try:
        return func(*args, **kwargs)
    except CLIError as e:
        handle_exception(e)
        return None
    except Exception as e:
        handle_exception(e)
        raise