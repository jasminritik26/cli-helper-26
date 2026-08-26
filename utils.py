import time
import functools
import logging

logger = logging.getLogger("cli-helper-26")

def retry(max_attempts=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        logger.error(f"Operation {func.__name__} failed after {max_attempts} attempts.")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

def safe_request(url, timeout=5):
    """Simulated network request helper."""
    import urllib.request
    import urllib.error
    
    @retry(max_attempts=3, delay=0.5, exceptions=(urllib.error.URLError, TimeoutError))
    def _execute():
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.read().decode('utf-8')
            
    return _execute()
