import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_logger(
    name: str = "cli_helper",
    log_file: str = "logs/cli_helper.log",
    level: int = logging.INFO,
    max_bytes: int = 1048576,
    backup_count: int = 5,
) -> logging.Logger:
    """Configures and returns a logger with both console and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is already configured
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating File Handler
    try:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as err:
        # Fallback to console-only logging if file writing fails
        logger.warning(
            f"Failed to initialize file logger: {err}. Logging to console only."
        )

    return logger