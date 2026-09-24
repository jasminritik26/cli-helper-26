import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    """
    Decorator for retrying network operations with exponential backoff.
    
    :param max_attempts: Maximum number of retries.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier for the delay after each failure.
    :param exceptions: Tuple of exception types to trigger a retry.
    """
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
                    if attempts >= max_attempts:
                        logger.error(f"Final attempt {attempts} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator