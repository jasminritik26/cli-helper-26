import functools
import time
from typing import Callable, Any, Dict

# Cache for repetitive computational tasks
_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100) -> list:
    """Memory-efficient processing of large datasets."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def timed_execution(func: Callable) -> Callable:
    """Performance tracking for core functions."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        print(f"DEBUG: {func.__name__} executed in {duration:.4f}s")
        return result
    return wrapper

def clear_cache() -> None:
    """Memory management for memoization cache."""
    _cache.clear()