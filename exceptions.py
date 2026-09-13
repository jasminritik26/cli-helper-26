class CLIError(Exception):
    """Base exception for cli-helper-26."""
    pass

class ValidationError(CLIError):
    """Raised when input validation fails."""
    pass

class ConfigError(CLIError):
    """Raised when configuration loading fails."""
    pass

class ProcessingError(CLIError):
    """Raised when data transformation fails."""
    pass

_EXCEPTION_MAP = {
    'validation': ValidationError,
    'config': ConfigError,
    'processing': ProcessingError
}

def raise_helper_error(error_type: str, message: str):
    """
    Efficient exception instantiation using a cached lookup table.
    Avoids multiple conditional checks during runtime.
    """
    exception_class = _EXCEPTION_MAP.get(error_type, CLIError)
    raise exception_class(message)

if __name__ == "__main__":
    # Example of optimized exception triggering
    try:
        raise_helper_error('validation', 'Invalid input detected')
    except ValidationError as e:
        print(f"Caught expected error: {e}")