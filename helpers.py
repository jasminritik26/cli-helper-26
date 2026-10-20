import functools
import time
import logging

# Configure basic logger for operation tracking
logger = logging.getLogger(__name__)

def memoize_with_ttl(ttl_seconds=300):
    """Performance optimization: cache function results with TTL."""
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(items, batch_size=100):
    """Performance optimization: process items in memory-efficient chunks."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def fast_io_read(filepath):
    """Performance optimization: buffered file reading for speed."""
    try:
        with open(filepath, 'r', buffering=65536) as f:
            return f.readlines()
    except IOError as e:
        logger.error(f"Failed to read file {filepath}: {e}")
        return []