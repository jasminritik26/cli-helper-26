import sys

def validate_input(user_input):
    """Checks if input is non-empty and within character limits."""
    stripped = user_input.strip()
    if not stripped:
        return False, "Input cannot be empty."
    if len(stripped) > 255:
        return False, "Input exceeds maximum length of 255 characters."
    return True, stripped

def process_command(cmd):
    """Simulates processing of validated commands."""
    print(f"Processing: {cmd}")

def run_main_loop():
    """Main application loop with integrated validation logic."""
    print("CLI Helper 26 - Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input("> ")
            
            if user_input.lower() == 'exit':
                print("Exiting application.")
                break
                
            is_valid, result = validate_input(user_input)
            
            if not is_valid:
                print(f"Validation Error: {result}")
                continue
                
            process_command(result)
            
        except (KeyboardInterrupt, EOFError):
            print("\nShutting down...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_main_loop()