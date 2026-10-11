class ValidationError(Exception):
    """Custom exception for input validation errors."""
    pass

class InputValidator:
    """Validator for user input in main processing loop."""

    @staticmethod
    def validate_command(command: str) -> None:
        """Validates that command is not empty and within allowed set."""
        allowed = {'start', 'stop', 'status', 'exit'}
        
        if not command or not isinstance(command, str):
            raise ValidationError("Input command cannot be empty.")
        
        if command.strip().lower() not in allowed:
            raise ValidationError(f"Invalid command: {command}. Allowed: {allowed}")

    @staticmethod
    def validate_payload(data: str) -> str:
        """Validates payload constraints."""
        clean_data = data.strip()
        if len(clean_data) > 256:
            raise ValidationError("Payload length exceeds 256 characters.")
        return clean_data

def run_loop():
    """Main loop with integrated validation logic."""
    validator = InputValidator()
    
    while True:
        try:
            user_input = input("> ").strip()
            if user_input == "exit":
                break
            
            validator.validate_command(user_input)
            print(f"Processing: {user_input}")
            
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except EOFError:
            break