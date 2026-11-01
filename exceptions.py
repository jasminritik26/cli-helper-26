class CLIError(Exception):
    """Base exception for cli-helper-26."""
    pass

class ConfigurationError(CLIError):
    """Raised when config files are missing or malformed."""
    pass

class ValidationError(CLIError):
    """Raised when input parameters fail validation."""
    pass

class ProcessingError(CLIError):
    """Raised during core logic execution failure."""
    pass

def handle_error(err: Exception) -> None:
    """Maps internal exceptions to user-friendly messages."""
    if isinstance(err, ConfigurationError):
        print(f"Config Error: {err}")
    elif isinstance(err, ValidationError):
        print(f"Input Error: {err}")
    elif isinstance(err, ProcessingError):
        print(f"Runtime Error: {err}")
    else:
        print(f"Unexpected Error: {err}")