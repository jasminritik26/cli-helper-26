import logging
import sys
from typing import Optional

class DataLogger:
    """Utility for standardized application logging."""
    
    def __init__(self, name: str = "cli-helper-26", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # prevent duplicate handlers in interactive sessions
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def error(self, message: str, exc: Optional[Exception] = None) -> None:
        if exc:
            self.logger.error(f"{message}: {str(exc)}", exc_info=True)
        else:
            self.logger.error(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

def get_logger(name: str = "cli-helper-26") -> DataLogger:
    """Factory function for consistent logger instances."""
    return DataLogger(name)