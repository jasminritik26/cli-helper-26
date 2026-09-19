import sys
from typing import Dict, Any, List

class ValidationError(Exception):
    """Custom exception for input validation failures in the CLI."""
    pass

class CommandProcessor:
    """Processes and validates command-line input within a main loop."""
    
    def __init__(self, allowed_commands: List[str]):
        self.allowed_commands = allowed_commands

    def validate_input(self, raw_input: str) -> Dict[str, Any]:
        """Validates the format and content of the user input.
        
        Format should be: <command> [key=value key2=value2 ...]
        """
        cleaned = raw_input.strip()
        if not cleaned:
            raise ValidationError("Input cannot be empty")

        parts = cleaned.split()
        command = parts[0].lower()

        if command not in self.allowed_commands:
            raise ValidationError(f"Unknown command '{command}'. Allowed: {', '.join(self.allowed_commands)}")

        args = {}
        for param in parts[1:]:
            if '=' not in param:
                raise ValidationError(f"Invalid parameter format '{param}'. Expected key=value")
            key, val = param.split('=', 1)
            if not key.strip() or not val.strip():
                raise ValidationError(f"Key and value must not be empty in '{param}'")
            args[key.strip()] = val.strip()

        return {"command": command, "args": args}

    def run_loop(self) -> None:
        """Main processing loop designed for input handling and validation."""
        print("CLI Helper active. Type 'exit' to stop.")
        while True:
            try:
                user_input = input("cli-helper> ")
                if user_input.strip().lower() == "exit":
                    print("Exiting command processor.")
                    break

                parsed = self.validate_input(user_input)
                print(f"Processing success: {parsed['command']} with parameters {parsed['args']}")

            except ValidationError as ve:
                print(f"Validation Error: {ve}", file=sys.stderr)
            except (KeyboardInterrupt, EOFError):
                print("\nSession terminated.")
                break

if __name__ == "__main__":
    # Example instantiation for execution demonstration
    processor = CommandProcessor(allowed_commands=["config", "status", "deploy"])
    processor.run_loop()