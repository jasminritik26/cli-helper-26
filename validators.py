import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def validate_input_config(data: Any) -> bool:
    """Validates dictionary configuration structure."""
    try:
        if not isinstance(data, dict):
            raise ValueError("Configuration must be a dictionary")
        
        if not data:
            logger.warning("Empty configuration provided")
            return False
            
        if "version" not in data:
            raise KeyError("Missing mandatory field: version")
            
        return True
    except (ValueError, KeyError) as e:
        logger.error(f"Configuration validation error: {e}")
        return False
    except Exception as e:
        logger.critical(f"Unexpected error during validation: {e}")
        return False

def sanitize_path(path: Optional[str]) -> str:
    """Ensures path input is safe and valid."""
    if not path:
        logger.error("Null path provided for sanitization")
        return ""
    
    try:
        # Ensure path is string and remove null bytes
        cleaned_path = str(path).replace("\0", "")
        return cleaned_path.strip()
    except Exception as e:
        logger.error(f"Path sanitization failure: {e}")
        return ""