import logging
import sys
from typing import Optional

class CLIFormatter(logging.Formatter):
    """Standardizes log output format for the CLI application."""
    FORMAT = "%(levelname)s: %(message)s"

    def __init__(self) -> None:
        super().__init__(self.FORMAT)

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a consistent logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(CLIFormatter())
        logger.addHandler(handler)

    return logger

# Global instance for shared access across the package
app_logger = get_logger("cli-helper-26")