import os
import pathlib
from typing import Final

# Application configuration defaults
APP_NAME: Final[str] = "cli-helper-26"
VERSION: Final[str] = "1.0.0"

# Path constants
BASE_DIR: Final[pathlib.Path] = pathlib.Path(__file__).resolve().parent
DATA_DIR: Final[pathlib.Path] = BASE_DIR / "data"
LOG_DIR: Final[pathlib.Path] = BASE_DIR / "logs"

# Operational limits
MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[int] = 30
DEFAULT_ENCODING: Final[str] = "utf-8"

# Logging configuration
LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL: Final[str] = os.getenv("LOG_LEVEL", "INFO").upper()

# Supported file extensions for processing
SUPPORTED_EXTENSIONS: Final[list[str]] = [".txt", ".json", ".csv", ".yaml"]

# Environment validation
def ensure_directories() -> None:
    """Initializes required filesystem structure."""
    for directory in [DATA_DIR, LOG_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

# Execution on import
ensure_directories()