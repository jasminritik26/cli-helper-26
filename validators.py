import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(max_retries=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(f"Max retries reached. Final failure: {e}")
            
            raise last_exception
        return wrapper
    return decorator

def validate_network_response(response):
    """Basic validation for network response objects."""
    if response is None:
        return False
    if hasattr(response, 'status_code') and 200 <= response.status_code < 300:
        return True
    return False