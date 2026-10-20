class CLIHelperError(Exception):
    """Base exception for the cli-helper-26 project."""
    pass

class ConfigurationError(CLIHelperError):
    """Raised when config files are missing or malformed."""
    pass

class InputValidationError(CLIHelperError):
    """Raised when user input fails required schema checks."""
    pass

class ProcessingError(CLIHelperError):
    """Raised when core logic execution fails."""
    pass

def handle_cli_error(err: Exception) -> None:
    """Centralized error reporting for runtime exceptions."""
    if isinstance(err, CLIHelperError):
        print(f"[CLI Error] {err}")
    else:
        print(f"[Unexpected Error] {type(err).__name__}: {err}")

# Usage pattern:
# try:
#     # logic here
# except Exception as e:
#     handle_cli_error(e)
#     exit(1)