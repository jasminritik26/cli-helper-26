class CLIError(Exception):
    """Base exception for all cli-helper-26 errors."""
    pass

class ConfigurationError(CLIError):
    """Raised when configuration loading fails."""
    pass

class ValidationError(CLIError):
    """Raised when input validation fails."""
    pass

class ExecutionError(CLIError):
    """Raised when a command or process fails."""
    pass

def handle_exception(exc: Exception) -> str:
    """Returns a formatted error message for display."""
    if isinstance(exc, CLIError):
        return f"[CLI Error] {str(exc)}"
    return f"[Unexpected Error] {type(exc).__name__}: {str(exc)}"

def raise_if_none(value, name: str):
    """Helper to ensure required values exist."""
    if value is None:
        raise ValidationError(f"Missing required parameter: {name}")
    return value

def validate_path(path: str):
    """Verifies if a path exists for operations."""
    import os
    if not os.path.exists(path):
        raise ValidationError(f"Path not found: {path}")
    return True