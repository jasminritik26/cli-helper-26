import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=2, backoff=2, exceptions=(Exception,)):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed for {func.__name__}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def fetch_network_data(url):
    """Example network operation requiring retry logic."""
    # Simulated network call logic
    return {"status": "success", "url": url}