import functools
import time
from typing import Callable, Any

# Cache dictionary to store function results
_CACHE = {}

def memoize(func: Callable) -> Callable:
    """Performance decorator for expensive function calls."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

class DataProcessor:
    """Core processor with optimized data traversal."""
    def __init__(self, data: list):
        self.data = data

    def process_batch(self, multiplier: int) -> list:
        # Pre-allocate list and use list comprehension for speed
        return [x * multiplier for x in self.data]

def run_pipeline(items: list, factor: int) -> list:
    """Main execution entry point with timing instrumentation."""
    start_time = time.perf_counter()
    
    processor = DataProcessor(items)
    result = processor.process_batch(factor)
    
    duration = time.perf_counter() - start_time
    print(f"Execution completed in {duration:.6f} seconds")
    return result