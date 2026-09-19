import sys

def validate_input(user_input):
    """Ensures input is non-empty and within expected length."""
    if not user_input or not user_input.strip():
        return False, "Input cannot be empty."
    if len(user_input) > 255:
        return False, "Input exceeds maximum length of 255 characters."
    return True, None

def run_main_loop():
    """Main processing loop with integrated input validation."""
    print("cli-helper-26 initialized. Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input(">> ").strip()
            
            if user_input.lower() == 'exit':
                break
                
            is_valid, error_msg = validate_input(user_input)
            
            if not is_valid:
                print(f"Validation error: {error_msg}")
                continue
                
            # Process valid input here
            print(f"Processing: {user_input}")
            
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    run_main_loop()