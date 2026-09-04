import time
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry_operation(max_attempts=3, delay=1.0, exceptions=(Exception,)):
    """Decorator to retry a function if specified exceptions occur."""
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
                        logger.error(f"Final attempt failed for {func.__name__}")
                        raise e
                    logger.warning(f"Attempt {attempts} failed, retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_operation(max_attempts=3, delay=2.0, exceptions=(ConnectionError, TimeoutError))
def fetch_network_data(url):
    """Example function performing a network operation."""
    logger.info(f"Fetching data from {url}...")
    # Simulate network instability
    raise ConnectionError("Failed to reach server")

if __name__ == "__main__":
    try:
        fetch_network_data("https://api.example.com")
    except Exception as e:
        logger.error(f"Operation aborted: {e}")