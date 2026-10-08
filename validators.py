import re

class InputValidator:
    """Utility class for processing and validating cli user input."""

    @staticmethod
    def validate_command(user_input: str) -> bool:
        """Checks if input matches alphanumeric pattern."""
        return bool(re.match(r'^[a-zA-Z0-9_\s]+$', user_input.strip()))

    @staticmethod
    def sanitize(user_input: str) -> str:
        """Strips whitespace and converts to lowercase."""
        return user_input.strip().lower()

def process_main_loop():
    """Example main loop integration for cli-helper-26."""
    validator = InputValidator()
    
    while True:
        raw_input = input("cli-helper-26 > ")
        
        if raw_input.lower() in ['exit', 'quit']:
            break
            
        if not validator.validate_command(raw_input):
            print("Error: invalid characters detected in input.")
            continue
            
        clean_data = validator.sanitize(raw_input)
        print(f"Processing: {clean_data}")

if __name__ == "__main__":
    process_main_loop()