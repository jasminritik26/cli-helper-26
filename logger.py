import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "app.log"

def setup_logger(name: str = "cli-helper-26") -> logging.Logger:
    """Configures a rotating file logger."""
    if not LOG_DIR.exists():
        LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Rotate logs: max 5MB per file, keep 3 backups
        handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=5 * 1024 * 1024,
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Optional: Log to console as well
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger