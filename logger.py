import logging
import sys
import os
from typing import Optional

def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    """Configures a standardized logger with robust error handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    try:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if log_file:
            # Handle edge case: directory permission or path errors
            log_dir = os.path.dirname(os.path.abspath(log_file))
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)
            
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    except (OSError, PermissionError) as e:
        # Fallback to stderr if file logging fails
        print(f"Critical: Failed to initialize log file at {log_file}: {e}", file=sys.stderr)
        logger.setLevel(logging.WARNING)

    return logger