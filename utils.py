import functools
import time
from typing import Callable, Any, Dict

# LRU cache implementation for CPU-bound helper functions
# Limits memory usage while improving repeat execution speed
CACHE_SIZE = 128

def memoize(func: Callable) -> Callable:
    """Decorator for caching function results based on arguments."""
    cache: Dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            if len(cache) >= CACHE_SIZE:
                cache.pop(next(iter(cache)))
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Generator for efficient large data set handling."""
    for i in range(0, len(items), chunk_size):
        yield items[i : i + chunk_size]

def timed_execution(func: Callable):
    """Decorator for monitoring performance metrics of tasks."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution of {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper