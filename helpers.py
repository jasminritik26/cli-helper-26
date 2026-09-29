import functools
import time
import logging

# Configure logger for core operations
logger = logging.getLogger('cli-helper-26')

# Cache for compute-intensive function results
_CACHE = {}

def memoize_process(func):
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(data_list, chunk_size=100):
    """Generator for memory-efficient batch processing."""
    for i in range(0, len(data_list), chunk_size):
        yield data_list[i:i + chunk_size]

@memoize_process
def intensive_transform(data: str) -> str:
    """Example of an expensive string transformation."""
    time.sleep(0.1)
    return data.strip().upper()

def optimized_data_handler(items):
    """Batch processor using generator expressions."""
    results = []
    for batch in batch_process(items):
        transformed = [intensive_transform(item) for item in batch]
        results.extend(transformed)
    return results