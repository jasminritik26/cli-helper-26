import re

class InputValidator:
    """Handles input validation for cli-helper-26 commands."""

    @staticmethod
    def validate_command(cmd: str) -> bool:
        """Checks if the command follows alphanumeric pattern."""
        return bool(re.match(r"^[a-z0-9_-]{3,20}$", cmd.lower()))

    @staticmethod
    def validate_integer(value: str, min_val: int = 0, max_val: int = 100) -> int:
        """Parses and validates range constraints for numeric inputs."""
        try:
            val = int(value)
            if min_val <= val <= max_val:
                return val
            raise ValueError(f"Input {val} out of bounds")
        except ValueError:
            raise ValueError("Invalid numeric input provided")

def process_input_loop():
    """Main loop with validation layer."""
    validator = InputValidator()
    
    while True:
        user_input = input("Enter command (or 'exit'): ").strip()
        if user_input.lower() == 'exit':
            break
            
        try:
            if validator.validate_command(user_input):
                print(f"Processing: {user_input}")
            else:
                print("Error: Invalid command format")
        except Exception as e:
            print(f"Validation failure: {e}")