class CLIError(Exception):
    """Base exception for cli-helper-26."""
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

class ValidationError(CLIError):
    """Raised when input validation fails."""
    pass

class ConfigurationError(CLIError):
    """Raised when configuration loading fails."""
    pass

class ProcessingError(CLIError):
    """Raised when core processing tasks fail."""
    pass

# Pre-instantiated error messages for performance optimization
# to avoid repeated object creation in high-frequency loops
ERR_INVALID_INPUT = ValidationError("Invalid input provided", code=400)
ERR_CONFIG_MISSING = ConfigurationError("Configuration file missing", code=404)

def raise_if(condition, exception_instance):
    """Helper to raise pre-instantiated errors efficiently."""
    if condition:
        raise exception_instance

__all__ = [
    "CLIError",
    "ValidationError",
    "ConfigurationError",
    "ProcessingError",
    "ERR_INVALID_INPUT",
    "ERR_CONFIG_MISSING",
    "raise_if"
]