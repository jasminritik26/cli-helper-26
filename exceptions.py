class CLIHelperError(Exception):
    """Base exception for all cli-helper-26 errors."""
    pass

class ConfigurationError(CLIHelperError):
    """Raised when config validation fails."""
    pass

class ValidationError(CLIHelperError):
    """Raised when input parameters fail constraints."""
    pass

class ExecutionError(CLIHelperError):
    """Raised when a core process fails."""
    def __init__(self, message, exit_code=1):
        super().__init__(message)
        self.exit_code = exit_code

def raise_if_none(value, name):
    """Utility to validate mandatory configuration values."""
    if value is None:
        raise ValidationError(f"Mandatory value '{name}' cannot be None")

def handle_execution_context(func):
    """Decorator to wrap functions in generic error handlers."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CLIHelperError:
            raise
        except Exception as e:
            raise ExecutionError(f"Unexpected error: {str(e)}") from e
    return wrapper