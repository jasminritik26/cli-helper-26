import sys

def validate_input(user_input):
    """Checks if input is non-empty and within bounds."""
    if not user_input or not user_input.strip():
        return False, "Input cannot be empty."
    if len(user_input) > 256:
        return False, "Input exceeds maximum length of 256 characters."
    return True, None

def process_command(cmd):
    """Business logic for the CLI processing."""
    print(f"Processing: {cmd}")

def run_main_loop():
    """Main application loop with integrated validation."""
    print("cli-helper-26 initialized. Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input("> ")
            
            if user_input.lower() == 'exit':
                break
            
            is_valid, error_message = validate_input(user_input)
            
            if not is_valid:
                print(f"Validation Error: {error_message}", file=sys.stderr)
                continue
                
            process_command(user_input)
            
        except EOFError:
            break
        except Exception as e:
            print(f"Unexpected error: {e}", file=sys.stderr)

if __name__ == "__main__":
    run_main_loop()