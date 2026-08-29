"""Custom exceptions for cli-helper-26.
This module centralizes error definitions for the general CLI helper tool.
"""

from typing import Any, Optional, Dict


class CLIHelperBaseException(Exception):
    """Base class for CLI helper exceptions."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        self.message = message
        self.details = details or {}
        super().__init__(message)

    def to_dict(self) -> Dict[str, Any]:
        """Return a dict representation of the exception."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }


class ConfigError(CLIHelperBaseException):
    """Error related to configuration settings."""
    pass


class ArgumentError(CLIHelperBaseException):
    """Error for invalid command line arguments."""
    def __init__(self, arg_name: str, provided: str, expected: str) -> None:
        msg = f"Invalid argument '{arg_name}': got '{provided}', expected {expected}"
        super().__init__(msg, {"arg": arg_name, "provided": provided, "expected": expected})


class ProcessingError(CLIHelperBaseException):
    """Error during data processing or computation."""
    pass


class FileError(CLIHelperBaseException):
    """Error for input/output operations."""
    pass


class AccessDeniedError(CLIHelperBaseException):
    """Error when lacking permissions for an action."""
    pass


def get_error_message(exception: Exception) -> str:
    """Extract a clean error message for display."""
    if isinstance(exception, CLIHelperBaseException):
        return exception.message
    return str(exception)


def is_recoverable(exception: Exception) -> bool:
    """Check if the error is recoverable."""
    if isinstance(exception, (ConfigError, ArgumentError)):
        return False
    return True