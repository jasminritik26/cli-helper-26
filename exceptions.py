"""Custom exception classes for the CLI Helper library."""

from typing import Optional


class CLIHelperError(Exception):
    """Base exception class for all CLI Helper errors."""

    def __init__(self, message: str, exit_code: int = 1) -> None:
        """Initialize base CLI helper exception.

        Args:
            message: Human-readable error description.
            exit_code: Recommended process exit code for CLI context.
        """
        super().__init__(message)
        self.message: str = message
        self.exit_code: int = exit_code

    def __str__(self) -> str:
        return f"[Exit {self.exit_code}] {self.message}"


class CommandExecutionError(CLIHelperError):
    """Raised when an external shell command execution fails."""

    def __init__(
        self,
        message: str,
        command: str,
        exit_code: int = 1,
        stderr: Optional[str] = None,
    ) -> None:
        """Initialize command execution exception.

        Args:
            message: Description of the execution failure.
            command: The CLI command string that failed.
            exit_code: Exit status returned by the sub-process.
            stderr: Standard error output captured from execution.
        """
        super().__init__(message, exit_code=exit_code)
        self.command: str = command
        self.stderr: Optional[str] = stderr

    def detailed_report(self) -> str:
        """Format detailed failure output for CLI diagnostic logs.

        Returns:
            Multi-line string detailing command, status, and stderr.
        """
        output = [f"Command Failed: {self.command}", f"Exit Code: {self.exit_code}"]
        if self.stderr:
            output.append(f"Stderr: {self.stderr.strip()}")
        return "\n".join(output)


class ConfigurationError(CLIHelperError):
    """Raised when CLI configuration loading or validation fails."""

    def __init__(self, message: str, config_key: Optional[str] = None) -> None:
        """Initialize configuration error.

        Args:
            message: Description of the configuration issue.
            config_key: Optional configuration key associated with error.
        """
        super().__init__(message, exit_code=2)
        self.config_key: Optional[str] = config_key


class ValidationError(CLIHelperError):
    """Raised when CLI user input or argument validation fails."""

    def __init__(self, message: str, argument_name: Optional[str] = None) -> None:
        """Initialize validation error.

        Args:
            message: Details on validation criteria failure.
            argument_name: Name of the invalid CLI argument.
        """
        super().__init__(message, exit_code=2)
        self.argument_name: Optional[str] = argument_name
