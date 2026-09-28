import sys

def validate_input(user_input):
    """Checks if input is non-empty and alphanumeric."""
    if not user_input or not user_input.isalnum():
        return False
    return True

def run_processing_loop():
    """Main loop with input validation for cli-helper-26."""
    print("Starting cli-helper-26. Enter 'exit' to quit.")
    
    while True:
        try:
            user_input = input(">> ").strip()
            
            if user_input.lower() == 'exit':
                print("Exiting loop.")
                break
            
            if not validate_input(user_input):
                print("Error: invalid input. Please use alphanumeric characters.")
                continue
                
            process_data(user_input)
            
        except (KeyboardInterrupt, EOFError):
            print("\nSession terminated.")
            break

def process_data(data):
    """Placeholder for core logic."""
    print(f"Processing: {data}")

if __name__ == '__main__':
    run_processing_loop()