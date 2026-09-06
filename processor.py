import time
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry(exceptions, tries=3, delay=1, backoff=2):
    """Decorator for retrying functions with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"{e}, Retrying in {mdelay} seconds...")
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

class NetworkProcessor:
    def __init__(self, timeout=5):
        self.timeout = timeout

    @retry((ConnectionError, TimeoutError), tries=3, delay=2)
    def fetch_data(self, endpoint):
        """Simulate network operation with retry support."""
        logger.info(f"Attempting to fetch from {endpoint}")
        # Simulated conditional failure
        if "fail" in endpoint:
            raise ConnectionError("Failed to connect to server")
        return {"status": "success", "data": "sample payload"}

if __name__ == "__main__":
    processor = NetworkProcessor()
    try:
        result = processor.fetch_data("https://api.example.com/fail")
        print(result)
    except Exception as e:
        logger.error(f"Final failure after retries: {e}")