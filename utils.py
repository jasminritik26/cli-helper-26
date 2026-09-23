import os
import shutil
from pathlib import Path
from typing import Union

def ensure_directory(path: Union[str, Path]) -> None:
    """Create directory if it does not exist."""
    target = Path(path)
    if not target.exists():
        target.mkdir(parents=True, exist_ok=True)

def cleanup_temp_files(directory: str, extension: str = '.tmp') -> int:
    """Remove temporary files from a directory and return count."""
    count = 0
    dir_path = Path(directory)
    if not dir_path.is_dir():
        return count

    for item in dir_path.glob(f'*{extension}'):
        try:
            item.unlink()
            count += 1
        except OSError:
            continue
    return count

def format_byte_size(size: int) -> str:
    """Convert bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def get_file_metadata(path: Union[str, Path]) -> dict:
    """Retrieve basic file attributes as a dictionary."""
    file_path = Path(path)
    stats = file_path.stat()
    return {
        "name": file_path.name,
        "size": stats.st_size,
        "modified": stats.st_mtime
    }