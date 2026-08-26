import sys

class CLIInputValidator:
    """Validates command line inputs during the main processing loop."""
    
    def __init__(self, allowed_commands=None):
        self.allowed_commands = allowed_commands or ['run', 'status', 'exit', 'help']

    def validate_command(self, user_input: str) -> bool:
        """Check if the provided input string is a valid command."""
        if not user_input:
            return False
        
        cleaned_input = user_input.strip().lower()
        parts = cleaned_input.split()
        
        if not parts:
            return False
            
        command = parts[0]
        return command in self.allowed_commands

    def sanitize_arguments(self, user_input: str) -> list:
        """Sanitize and split user input into command and arguments."""
        if not self.validate_command(user_input):
            raise ValueError(f"Invalid command format: '{user_input}'")
            
        parts = user_input.strip().split()
        return parts

def process_loop_input(raw_input: str) -> tuple:
    """Main entry point for input validation in processing loop."""
    validator = CLIInputValidator()
    
    try:
        tokens = validator.sanitize_arguments(raw_input)
        return tokens[0], tokens[1:]
    except ValueError as e:
        print(f"Validation Error: {e}", file=sys.stderr)
        return None, []
