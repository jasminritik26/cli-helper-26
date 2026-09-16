import sys
from typing import Optional

class CLIHelperError(Exception):
    """Base exception class for all cli-helper errors."""
    def __init__(self, message: str, exit_code: int = 1) -> None:
        super().__init__(message)
        self.message = message
        self.exit_code = exit_code

    def print_and_exit(self) -> None:
        """Prints the formatted error message to stderr and exits."""
        sys.stderr.write(f"[Error] {self.message}\n")
        sys.exit(self.exit_code)

class ConfigurationError(CLIHelperError):
    """Raised when CLI configuration is missing or invalid."""
    def __init__(self, message: str) -> None:
        super().__init__(message, exit_code=2)

class ValidationError(CLIHelperError):
    """Raised when input parameters or arguments fail validation."""
    def __init__(self, message: str) -> None:
        super().__init__(message, exit_code=3)

class CommandExecutionError(CLIHelperError):
    """Raised when an external or internal CLI command fails to execute."""
    def __init__(self, message: str, original_error: Optional[Exception] = None) -> None:
        details = f" (Reason: {str(original_error)})" if original_error else ""
        super().__init__(f"{message}{details}", exit_code=4)
        self.original_error = original_error
