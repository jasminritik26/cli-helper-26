class CLIHelperError(Exception):
    """Base exception for all cli-helper-26 errors."""
    pass

class ConfigurationError(CLIHelperError):
    """Raised when configuration loading or parsing fails."""
    pass

class ValidationError(CLIHelperError):
    """Raised when input validation fails."""
    pass

class ProcessingError(CLIHelperError):
    """Raised during core logic execution failures."""
    pass

class ResourceNotFoundError(CLIHelperError):
    """Raised when a requested resource is missing."""
    pass

def handle_exception(e: Exception) -> None:
    """Standardized exception formatting for the CLI."""
    if isinstance(e, CLIHelperError):
        print(f"[ERROR] {e.__class__.__name__}: {str(e)}")
    else:
        print(f"[CRITICAL] An unexpected error occurred: {str(e)}")