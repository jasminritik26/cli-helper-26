import logging
import sys
from typing import Optional

class CLIFormatter(logging.Formatter):
    """Custom formatter for terminal output color coding."""
    FORMATS = {
        logging.DEBUG: "[DEBUG] %(message)s",
        logging.INFO: "%(message)s",
        logging.WARNING: "[WARNING] %(message)s",
        logging.ERROR: "[ERROR] %(message)s",
        logging.CRITICAL: "[CRITICAL] %(message)s"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Factory for consistent application logging setup."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(CLIFormatter())
        logger.addHandler(handler)

    return logger

def log_execution_time(func):
    """Decorator for monitoring function execution performance."""
    import time
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution of {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper