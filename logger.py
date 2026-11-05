import logging
import sys
from typing import Optional

class CLIFormatter(logging.Formatter):
    """Custom formatter for consistent CLI output styling."""
    FORMATS = {
        logging.DEBUG: "[DEBUG] %(message)s",
        logging.INFO: "%(message)s",
        logging.WARNING: "[WARNING] %(message)s",
        logging.ERROR: "[ERROR] %(message)s",
        logging.CRITICAL: "[CRITICAL] %(message)s"
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Initializes and returns a configured application logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(CLIFormatter())
        logger.addHandler(handler)

    return logger

# Global logger instance for the CLI project
cli_logger = get_logger("cli-helper-26")