import logging
import sys
from typing import Optional

# Configure standard formatting for cli-helper-26
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Initializes a standardized logger instance for the CLI application.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if get_logger is called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_data_summary(data: list, logger: logging.Logger) -> None:
    """
    Logs a summary of processed data items.
    """
    if not data:
        logger.warning("No data provided for summary.")
        return

    logger.info(f"Processed {len(data)} items successfully.")

def setup_debug_mode(enabled: bool) -> None:
    """
    Global toggle for application debug logging.
    """
    level = logging.DEBUG if enabled else logging.INFO
    logging.basicConfig(level=level, format=FORMAT)
