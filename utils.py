import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(max_attempts=3, delay=2.0, backoff=2.0, exceptions=(Exception,)):
    """Decorator to retry network or flaky operations with exponential backoff."""
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
                        logger.error(f"Operation '{func.__name__}' failed after {max_attempts} attempts.")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed for '{func.__name__}': {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
                    
        return wrapper
    return decorator

def safe_network_call(url, client_session, timeout=10):
    """Helper to execute standard GET requests with applied retry logic."""
    @retry_operation(max_attempts=3, delay=1.0, backoff=1.5)
    def _execute():
        response = client_session.get(url, timeout=timeout)
        response.raise_for_status()
        return response
    
    return _execute()
