import functools
from typing import Any, Callable

# Cache for repetitive data transformation results
_memoization_cache = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function results to improve throughput."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

class DataProcessor:
    """Core processor with performance-oriented batch handling."""
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    @memoize
    def transform(self, data: str) -> str:
        """Heavy transformation logic optimized with memoization."""
        return data.strip().lower()

    def process_batch(self, items: list[str]) -> list[str]:
        """Bulk processing implementation for reduced overhead."""
        results = []
        for i in range(0, len(items), self.batch_size):
            batch = items[i:i + self.batch_size]
            results.extend([self.transform(item) for item in batch])
        return results

def clear_cache() -> None:
    """Manual cache invalidation for memory management."""
    _memoization_cache.clear()