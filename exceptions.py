class CLIHelperError(Exception):
    """Base exception for cli-helper-26."""
    pass

class ConfigurationError(CLIHelperError):
    """Raised when configuration loading fails."""
    pass

class ValidationError(CLIHelperError):
    """Raised when input validation fails."""
    pass

class ProcessingError(CLIHelperError):
    """Raised during data processing tasks."""
    pass

class InitializationError(CLIHelperError):
    """Raised when core components fail to start."""
    pass

def handle_exception(exc: Exception) -> None:
    """Centralized error reporting for CLI operations."""
    if isinstance(exc, CLIHelperError):
        print(f"[ERROR] {exc.__class__.__name__}: {str(exc)}")
    else:
        print(f"[CRITICAL] Unexpected error: {str(exc)}")