import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class InputValidationError(Exception):
    """Custom exception raised when command input validation fails."""
    pass


def validate_payload(data: Any) -> Dict[str, Any]:
    """Validate raw input data structure before main execution."""
    if not isinstance(data, dict):
        raise InputValidationError("Payload must be a key-value dictionary")
    
    if "command" not in data or not isinstance(data["command"], str):
        raise InputValidationError("Payload missing required string field 'command'")
    
    data["command"] = data["command"].strip().lower()
    if not data["command"]:
        raise InputValidationError("Field 'command' cannot be empty or whitespace")
    
    return data


def process_batch_loop(items: List[Any]) -> List[Dict[str, Any]]:
    """Main batch processing loop with inline input validation."""
    processed_results = []
    
    for idx, raw_item in enumerate(items):
        try:
            validated = validate_payload(raw_item)
            cmd = validated["command"]
            payload = validated.get("data", {})
            
            logger.info(f"Processing item {idx}: command='{cmd}'")
            
            # Execution logic for valid commands
            if cmd == "ping":
                result = {"status": "pong", "details": payload}
            elif cmd == "format":
                result = {"formatted": str(payload).upper()}
            else:
                raise InputValidationError(f"Unsupported command type: '{cmd}'")
            
            processed_results.append({"index": idx, "success": True, "result": result})
            
        except InputValidationError as err:
            logger.warning(f"Validation failed at item {idx}: {err}")
            processed_results.append({"index": idx, "success": False, "error": str(err)})
            
    return processed_results
