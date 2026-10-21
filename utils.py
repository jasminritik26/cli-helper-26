import functools
import time
import logging
from typing import Callable, Any

logger = logging.getLogger('cli-helper-26')

def memoize(func: Callable) -> Callable:
    """Cache function results based on arguments."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def timer(func: Callable) -> Callable:
    """Measure execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        logger.debug(f'{func.__name__} executed in {duration:.4f} seconds')
        return result
    return wrapper

def batch_process(items: list, batch_size: int = 100):
    """Generator for chunking large lists into batches."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def fast_lookup_dict(items: list, key_attr: str) -> dict:
    """Convert list to dictionary for O(1) lookups."""
    return {getattr(i, key_attr): i for i in items}