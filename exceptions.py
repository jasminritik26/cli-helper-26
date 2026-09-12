class CLIHelperError(Exception):
    """Base exception for cli-helper-26."""
    pass

class ConfigurationError(CLIHelperError):
    """Raised when config files are missing or malformed."""
    pass

class ValidationError(CLIHelperError):
    """Raised during input or parameter validation."""
    pass

class ProcessingError(CLIHelperError):
    """Raised during core logic execution failures."""
    pass

class HandlerError(CLIHelperError):
    """Raised when command handlers fail to execute."""
    pass

def format_error(exc: Exception) -> str:
    """Helper to format exceptions into user-friendly strings."""
    if isinstance(exc, CLIHelperError):
        return f"[CLI Error] {exc.__class__.__name__}: {str(exc)}"
    return f"[Unexpected Error] {str(exc)}"