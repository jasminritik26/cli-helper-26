import sys
import argparse
from typing import Callable, Dict, Any, List, Optional, Tuple


class CommandRegistry:
    """Central registry and execution manager for CLI commands."""

    def __init__(self, description: str = "CLI Helper Tool"):
        self.parser = argparse.ArgumentParser(description=description)
        self.subparsers = self.parser.add_subparsers(dest="command", help="Available subcommands")
        self._handlers: Dict[str, Tuple[Callable[..., Any], Any]] = {}

    def register(self, name: str, help_text: str = "") -> Callable:
        """Decorator to register a function as a CLI subcommand."""
        def decorator(func: Callable) -> Callable:
            subparser = self.subparsers.add_parser(name, help=help_text)
            self._handlers[name] = (func, subparser)
            return func
        return decorator

    def add_argument(self, command_name: str, *args: Any, **kwargs: Any) -> None:
        """Attach an argument to a specific subcommand parser."""
        if command_name in self._handlers:
            _, subparser = self._handlers[command_name]
            subparser.add_argument(*args, **kwargs)

    def execute(self, args: Optional[List[str]] = None) -> Any:
        """Parse arguments and dispatch execution to the registered command."""
        parsed_args = self.parser.parse_args(args)
        if not parsed_args.command:
            self.parser.print_help()
            sys.exit(1)

        func, _ = self._handlers[parsed_args.command]
        arg_dict = vars(parsed_args)
        arg_dict.pop("command")
        return func(**arg_dict)


# Default engine instance for modular command setup
engine = CommandRegistry()
