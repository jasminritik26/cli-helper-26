import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str, log_file: str = 'app.log') -> logging.Logger:
    """Creates a rotating file logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if get_logger is called repeatedly
    if not logger.handlers:
        # Format: timestamp - name - level - message
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # 5MB file rotation, keeping 3 backup files
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Stream handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger