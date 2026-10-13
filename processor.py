import time
import functools
import logging

# Configure basic logger for network events
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry_operation(max_attempts=3, delay=2, backoff=2):
    """Decorator for retrying functions on exception"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    logger.warning(f"Attempt {attempts} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(max_attempts=3)
def fetch_remote_data(url):
    """Simulates a network request that may fail"""
    logger.info(f"Requesting {url}")
    # Simulate network instability
    import random
    if random.random() < 0.7:
        raise ConnectionError("Service unavailable")
    return {"status": "success", "data": "sample payload"}