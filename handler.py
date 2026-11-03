from typing import List, Dict, Optional, Any

class RequestHandler:
    """Handles incoming CLI requests and routes them to processors."""

    def __init__(self, debug: bool = False) -> None:
        self.debug: bool = debug
        self.history: List[Dict[str, Any]] = []

    def validate_request(self, payload: Dict[str, Any]) -> bool:
        """Checks if the payload contains required command fields."""
        required_fields = {"command", "args"}
        return required_fields.issubset(payload.keys())

    def process_command(self, payload: Dict[str, Any]) -> Optional[str]:
        """
        Executes the logic based on provided command string.
        Returns a status message or None if processing fails.
        """
        if not self.validate_request(payload):
            return "Invalid payload format"

        command: str = payload["command"]
        args: List[str] = payload.get("args", [])

        # Simulation of command routing logic
        result = f"Executed {command} with {len(args)} arguments"
        self.history.append({"cmd": command, "status": "success"})
        
        if self.debug:
            print(f"[DEBUG] {result}")
            
        return result

    def get_session_history(self) -> List[Dict[str, Any]]:
        """Returns the list of previously processed commands."""
        return self.history