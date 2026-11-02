import sys

def validate_input(user_input):
    """Ensures user input is non-empty and within character limits."""
    stripped = user_input.strip()
    if not stripped:
        return False, "Input cannot be empty."
    if len(stripped) > 100:
        return False, "Input exceeds maximum length of 100 characters."
    return True, stripped

def run_main_loop():
    """Main processing loop with integrated input validation."""
    print("CLI Helper 26 initialized. Type 'exit' to quit.")
    
    while True:
        try:
            raw_input = input(">>> ")
            
            if raw_input.lower() == 'exit':
                print("Exiting program.")
                break
            
            is_valid, result = validate_input(raw_input)
            
            if not is_valid:
                print(f"Validation error: {result}")
                continue
                
            # Processing logic for validated input
            process_command(result)
            
        except (KeyboardInterrupt, EOFError):
            print("\nShutting down gracefully.")
            break

def process_command(cmd):
    """Placeholder for actual business logic execution."""
    print(f"Processing command: {cmd}")

if __name__ == "__main__":
    run_main_loop()