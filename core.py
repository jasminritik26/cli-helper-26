from typing import List, Optional, Dict, Any

class CLIHandler:
    """Handles command execution and argument processing for cli-helper-26."""

    def __init__(self, name: str, debug: bool = False) -> None:
        self.name: str = name
        self.debug: bool = debug
        self.registry: Dict[str, Any] = {}

    def register_command(self, cmd: str, func: Any) -> None:
        """Registers a new command function to the internal registry."""
        self.registry[cmd] = func

    def execute(self, cmd: str, *args: str) -> Optional[Any]:
        """Executes a registered command with provided arguments."""
        if cmd not in self.registry:
            if self.debug:
                print(f"Command {cmd} not found.")
            return None
        
        return self.registry[cmd](*args)

    def get_status(self) -> Dict[str, str]:
        """Returns the current status of the CLI handler instance."""
        return {"name": self.name, "registered": str(len(self.registry))}

def format_output(data: List[str], prefix: str = "> ") -> str:
    """Formats a list of strings into a standard CLI output block."""
    return "\n".join([f"{prefix}{item}" for item in data])