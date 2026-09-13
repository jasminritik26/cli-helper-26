import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "cli_helper", log_file: str = "cli_helper.log", level: int = logging.INFO) -> logging.Logger:
    """Sets up a logger with console and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.hasHandlers():
        return logger

    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_formatter = logging.Formatter(
        "%(levelname)s: %(message)s"
    )

    try:
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5000000, backupCount=3, encoding="utf-8"
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    except OSError:
        pass

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger