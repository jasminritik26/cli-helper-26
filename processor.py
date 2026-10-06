import re
import sys
from typing import Dict, Any

class ValidationError(Exception):
    """Raised when input validation fails."""
    pass

class CLIProcessor:
    """Processes and validates CLI commands from the user input loop."""

    def __init__(self):
        self.allowed_commands = {"help", "exit", "version", "run", "config"}
        self.command_pattern = re.compile(r"^[a-zA-Z0-9_\-\s]+$")

    def validate_raw_input(self, user_input: str) -> str:
        """Validates basic shell inputs for safety and length."""
        cleaned = user_input.strip()
        if not cleaned:
            raise ValidationError("Input cannot be empty")
        if len(cleaned) > 200:
            raise ValidationError("Input exceeds maximum length of 200 characters")
        if not self.command_pattern.match(cleaned):
            raise ValidationError("Input contains invalid characters")
        return cleaned

    def parse_command(self, validated_input: str) -> Dict[str, Any]:
        """Parses and validates the command structures and arguments."""
        parts = validated_input.split()
        cmd = parts[0].lower()

        if cmd not in self.allowed_commands:
            raise ValidationError(f"Unknown command: '{cmd}'. Type 'help' for options")

        return {
            "command": cmd,
            "args": parts[1:]
        }

    def process_loop(self) -> None:
        """Main CLI input processing loop with strict validation."""
        print("CLI Helper Processor Started. Type 'help' for commands, 'exit' to quit.")
        while True:
            try:
                user_input = input("cli-helper> ")
                validated = self.validate_raw_input(user_input)
                parsed = self.parse_command(validated)

                if parsed["command"] == "exit":
                    print("Exiting CLI Helper.")
                    break
                elif parsed["command"] == "help":
                    print(f"Available commands: {', '.join(sorted(self.allowed_commands))}")
                elif parsed["command"] == "version":
                    print("cli-helper-26 v1.0.0")
                elif parsed["command"] == "run":
                    if not parsed["args"]:
                        raise ValidationError("Command 'run' requires at least one argument")
                    print(f"Executing action with: {parsed['args']}")
                elif parsed["command"] == "config":
                    print(f"Configuration parameter adjusted: {parsed['args']}")

            except ValidationError as ve:
                print(f"Validation Error: {ve}", file=sys.stderr)
            except KeyboardInterrupt:
                print("\nSession interrupted. Exiting.")
                break
