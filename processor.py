import sys
from typing import Dict, Any, List

def validate_input(user_input: str) -> Dict[str, Any]:
    """Validate and parse user command string into a structured format."""
    cleaned = user_input.strip()
    if not cleaned:
        raise ValueError("Input cannot be empty")
    
    parts = cleaned.split()
    command = parts[0].lower()
    allowed_commands = {"help", "run", "status", "exit"}
    
    if command not in allowed_commands:
        raise ValueError(f"Unknown command '{command}'. Allowed: {', '.join(allowed_commands)}")
        
    return {"command": command, "args": parts[1:]}

def process_loop() -> None:
    """Main interactive loop with robust input validation."""
    print("CLI Helper 26 initialized. Type 'exit' to quit.")
    
    while True:
        try:
            raw_input = input("cli-helper> ")
            parsed = validate_input(raw_input)
            
            cmd = parsed["command"]
            args = parsed["args"]
            
            if cmd == "exit":
                print("Exiting application...")
                break
            elif cmd == "help":
                print("Available commands: help, run <task>, status, exit")
            elif cmd == "status":
                print("System status: Ready")
            elif cmd == "run":
                if not args:
                    print("Error: 'run' command requires a task argument")
                    continue
                print(f"Running task: {args[0]}")
                
        except (KeyboardInterrupt, EOFError):
            print("\nSession terminated.")
            break
        except ValueError as err:
            print(f"Validation error: {err}")

if __name__ == "__main__":
    process_loop()