import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_operation(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying functions on exception."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            local_retries = retries
            current_delay = delay
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    local_retries -= 1
                    if local_retries < 0:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    
                    logger.warning(f"Retrying in {current_delay}s... (Attempts left: {local_retries})")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(retries=3, delay=2.0)
def network_request_wrapper(request_func: Callable, *args, **kwargs):
    """Example usage for external network calls."""
    return request_func(*args, **kwargs)