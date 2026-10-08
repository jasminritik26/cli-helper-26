import logging
import functools
from typing import Callable, Any

# Configure global logger for cli-helper-26
logger = logging.getLogger('cli_helper')
logger.setLevel(logging.INFO)

# Cache for memoized function results to optimize performance
_cache = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching repetitive function results."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

def log_performance(func: Callable) -> Callable:
    """Decorator for tracking execution time of critical functions."""
    import time
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        if duration > 0.1:
            logger.warning(f'Performance bottleneck in {func.__name__}: {duration:.4f}s')
        return result
    return wrapper

def clear_cache() -> None:
    """Manual cache invalidation for memory management."""
    _cache.clear()
    logger.info('Logger cache cleared successfully')