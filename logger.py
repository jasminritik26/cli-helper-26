import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance for the application.

    Args:
        name: The name of the logger instance.
        level: The logging threshold level.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_message(logger: logging.Logger, message: str, level: str = "info") -> None:
    """
    Helper to log messages with dynamic severity levels.

    Args:
        logger: The logger instance to use.
        message: The text string to log.
        level: The severity level as a string.
    """
    levels = {
        "debug": logger.debug,
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "critical": logger.critical
    }

    log_func = levels.get(level.lower(), logger.info)
    log_func(message)