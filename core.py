import sys
from typing import List, Optional

class CLIHandler:
    """Core controller for CLI interaction management."""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.commands = {}

    def register_command(self, name: str, func: callable) -> None:
        """Registers a callback for a specific command keyword."""
        self.commands[name] = func

    def run(self, args: List[str]) -> None:
        """Parses arguments and executes matching command."""
        if not args:
            print("Usage: cli-helper-26 <command>")
            return

        command_name = args[0]
        if command_name in self.commands:
            try:
                self.commands[command_name](args[1:])
            except Exception as e:
                self._handle_error(e)
        else:
            print(f"Unknown command: {command_name}")

    def _handle_error(self, error: Exception) -> None:
        """Centralized error reporting."""
        print(f"Error: {error}", file=sys.stderr)
        if self.debug:
            import traceback
            traceback.print_exc()

def main():
    """Entry point for CLI execution."""
    handler = CLIHandler(debug=False)
    # Execution logic
    handler.run(sys.argv[1:])

if __name__ == "__main__":
    main()