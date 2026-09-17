import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(max_attempts=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator to retry network operations on specific exceptions.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    sleep_time = delay * (2 ** (attempts - 1))
                    logger.warning(f"Attempt {attempts} failed, retrying in {sleep_time}s...")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=1)
def fetch_network_resource(url):
    """
    Example network call wrapper.
    """
    # Simulate network operation
    logger.info(f"Fetching data from {url}")
    return {"status": "success", "data": "example payload"}