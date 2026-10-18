import sys
import functools
from typing import Callable, Any, Optional


class CLIError(Exception):
    """Base exception class for CLI helper errors."""
    def __init__(self, message: str, exit_code: int = 1):
        super().__init__(message)
        self.message = message
        self.exit_code = exit_code


class CommandNotFoundError(CLIError):
    """Raised when a requested CLI command is not recognized."""
    def __init__(self, command: str):
        super().__init__(f"Unknown command '{command}'. Use --help to list commands.", exit_code=2)


class InvalidArgumentError(CLIError):
    """Raised when command arguments fail validation or format checks."""
    def __init__(self, arg_name: str, reason: str):
        super().__init__(f"Invalid value for '{arg_name}': {reason}", exit_code=2)


class SystemExecutionError(CLIError):
    """Raised when an underlying system subprocess fails unexpectedly."""
    def __init__(self, process_name: str, stderr: Optional[str] = None):
        msg = f"Subprocess '{process_name}' execution failed."
        if stderr:
            msg += f" Details: {stderr.strip()}"
        super().__init__(msg, exit_code=3)


def safe_cli_execution(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator catching unhandled exceptions and routing CLI exit codes."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except CLIError as err:
            print(f"Error: {err.message}", file=sys.stderr)
            sys.exit(err.exit_code)
        except KeyboardInterrupt:
            print("\nOperation aborted by user.", file=sys.stderr)
            sys.exit(130)
        except Exception as err:
            print(f"Fatal internal error: {str(err)}", file=sys.stderr)
            sys.exit(1)
    return wrapper
