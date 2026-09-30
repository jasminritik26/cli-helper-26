import time
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def retry(retries=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    """
    Decorator to retry a function call with exponential backoff.
    
    :param retries: Number of retry attempts before giving up.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to delay after each retry.
    :param exceptions: A tuple of exceptions to catch and retry on.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(f"Failed '{func.__name__}' after {retries} attempts. Error: {e}")
                        raise e
                    
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed for '{func.__name__}'. "
                        f"Retrying in {attempt_delay:.2f} seconds... Error: {e}"
                    )
                    time.sleep(attempt_delay)
                    attempt_delay *= backoff
        return wrapper
    return decorator
