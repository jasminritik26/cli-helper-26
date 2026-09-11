import sys

def validate_input(user_input):
    """Ensures input is non-empty and within bounds."""
    stripped = user_input.strip()
    if not stripped:
        return False, "Input cannot be empty."
    if len(stripped) > 256:
        return False, "Input exceeds character limit."
    return True, stripped

def run_main_loop():
    """Main processing loop with validation."""
    print("CLI Helper 26 initialized. Type 'exit' to quit.")
    
    while True:
        try:
            raw = input("> ")
            if raw.lower() == 'exit':
                break
            
            is_valid, data = validate_input(raw)
            if not is_valid:
                print(f"Validation error: {data}")
                continue
            
            # Processing logic placeholder
            print(f"Processing: {data}")
            
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    run_main_loop()