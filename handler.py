import sys
from typing import Callable, Dict, List, Any, Optional

class CommandHandler:
    """Manages registration and execution of CLI commands."""

    def __init__(self) -> None:
        """Initialize the command handler with an empty command registry."""
        self._commands: Dict[str, Callable[..., Any]] = {}

    def register(self, name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """Decorator to register a function as a CLI command.

        Args:
            name: The string trigger for the command.
        """
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            self._commands[name] = func
            return func
        return decorator

    def execute(self, name: str, *args: Any, **kwargs: Any) -> Optional[Any]:
        """Execute a registered command with positional and keyword arguments.

        Args:
            name: The name of the command to execute.
            *args: Positional arguments passed to the command function.
            **kwargs: Keyword arguments passed to the command function.

        Returns:
            The return value of the executed command function, or None if failed.
        """
        if name not in self._commands:
            print(f"Error: Command '{name}' is not registered.", file=sys.stderr)
            return None
        
        try:
            return self._commands[name](*args, **kwargs)
        except TypeError as err:
            print(f"Error: Invalid arguments for command '{name}': {err}", file=sys.stderr)
            return None
        except Exception as err:
            print(f"Unhandled exception in command '{name}': {err}", file=sys.stderr)
            raise err

    def get_registered_commands(self) -> List[str]:
        """Retrieve a list of all currently registered command names.

        Returns:
            A list of sorted command string identifiers.
        """
        return sorted(list(self._commands.keys()))