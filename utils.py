import os
from typing import List, Optional, Union

def format_path(path: str) -> str:
    """Normalize and expand user paths for consistency."""
    return os.path.abspath(os.path.expanduser(path))

def chunk_list(data: List[Union[str, int]], size: int) -> List[List[Union[str, int]]]:
    """Split a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    return [data[i:i + size] for i in range(0, len(data), size)]

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieve environment variable with an optional fallback default."""
    return os.environ.get(key, default)

def sanitize_input(user_input: str) -> str:
    """Clean whitespace and convert input to lowercase for comparison."""
    return str(user_input).strip().lower()

def list_files_in_dir(directory: str, extension: Optional[str] = None) -> List[str]:
    """Return a list of files in a directory, optionally filtered by extension."""
    try:
        files = os.listdir(directory)
        if extension:
            return [f for f in files if f.endswith(extension)]
        return files
    except FileNotFoundError:
        return []