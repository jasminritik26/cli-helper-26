import sys
import json
from pathlib import Path

def load_json_file(file_path: str) -> dict:
    """Load and parse a JSON file safely with path expansion."""
    path = Path(file_path).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Target file not found: {path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {path}: {e}")

def save_json_file(file_path: str, data: dict, indent: int = 4) -> None:
    """Serialize dictionary to a JSON file with pretty printing."""
    path = Path(file_path).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent)

def format_output(data: any, as_json: bool = False) -> str:
    """Format data structure for CLI output presentation."""
    if as_json:
        return json.dumps(data, indent=2)
    if isinstance(data, (dict, list)):
        return json.dumps(data, indent=2)
    return str(data)

def safe_print(message: str, error: bool = False) -> None:
    """Print message to standard output or standard error stream."""
    stream = sys.stderr if error else sys.stdout
    print(message, file=stream)
