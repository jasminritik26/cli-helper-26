"""Custom exception classes for the cli-helper-26 package."""

from typing import Optional


class CLIHelperError(Exception):
    """Base exception class for all cli-helper errors."""

    def __init__(self, message: str) -> None:
        """Initialize the base exception with a message.

        Args:
            message: A descriptive error message.
        """
        super().__init__(message)
        self.message: str = message


class CommandExecutionError(CLIHelperError):
    """Raised when a CLI command fails to execute."""

    def __init__(self, message: str, return_code: Optional[int] = None) -> None:
        """Initialize the execution exception with a message and optional return code.

        Args:
            message: A descriptive error message.
            return_code: The exit status code of the failed command.
        """
        super().__init__(message)
        self.return_code: Optional[int] = return_code


class ValidationError(CLIHelperError):
    """Raised when input validation or parameter verification fails."""

    def __init__(self, message: str, parameter: Optional[str] = None) -> None:
        """Initialize the validation exception.

        Args:
            message: A descriptive error message.
            parameter: The name of the invalid parameter.
        """
        super().__init__(message)
        self.parameter: Optional[str] = parameter


class ConfigurationError(CLIHelperError):
    """Raised when configuration values are missing or invalid."""
