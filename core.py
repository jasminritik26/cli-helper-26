import functools
import time
from typing import Callable, Any

# global cache for performance-critical path execution
_CACHE = {}

def memoize_compute(func: Callable) -> Callable:
    """decorator for persistent caching of expensive operations"""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """generator for memory-efficient data chunking"""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class CoreProcessor:
    """main processing engine with optimization layers"""
    def __init__(self):
        self.start_time = time.time()

    @memoize_compute
    def transform_data(self, dataset: tuple) -> list:
        # simulated expensive computation optimized by caching
        return [x * 2 for x in dataset]

    def execute(self, items: list):
        """optimized execution loop using batching"""
        results = []
        for batch in batch_process(items):
            results.extend(self.transform_data(tuple(batch)))
        return results