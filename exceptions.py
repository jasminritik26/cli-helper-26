class CLIHelperError(Exception):
    """Base exception for cli-helper-26."""
    pass

class ConfigurationError(CLIHelperError):
    """Raised when config validation fails."""
    pass

class ProcessingError(CLIHelperError):
    """Raised when a data transformation fails."""
    pass

class ValidationError(CLIHelperError):
    """Raised when user input fails requirements."""
    pass

def raise_error(error_type: type, message: str):
    """Helper to instantiate and raise custom exceptions."""
    if not issubclass(error_type, CLIHelperError):
        raise ValueError("Exception must inherit from CLIHelperError")
    raise error_type(message)

def format_exception(e: Exception) -> str:
    """Standardizes exception messages for CLI output."""
    if isinstance(e, CLIHelperError):
        return f"[Error]: {str(e)}"
    return f"[Unexpected Error]: {type(e).__name__} - {str(e)}"