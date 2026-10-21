import sys

def validate_input(user_input):
    """Ensures user input is non-empty and within length constraints."""
    stripped = user_input.strip()
    if not stripped:
        return False, "Input cannot be empty."
    if len(stripped) > 100:
        return False, "Input exceeds maximum character limit of 100."
    return True, stripped

def process_command(cmd):
    """Executes business logic for valid commands."""
    print(f"Processing: {cmd}")

def run_main_loop():
    """Main entry point for command processing with validation."""
    print("CLI-Helper-26 initialized. Type 'exit' to quit.")
    
    while True:
        try:
            user_raw = input("> ")
            if user_raw.lower() == 'exit':
                break
            
            is_valid, result = validate_input(user_raw)
            
            if not is_valid:
                print(f"Validation error: {result}")
                continue
            
            process_command(result)
            
        except (EOFError, KeyboardInterrupt):
            break
        except Exception as e:
            print(f"Unexpected system error: {e}")

if __name__ == '__main__':
    run_main_loop()