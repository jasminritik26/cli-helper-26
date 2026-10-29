import time
import functools
import requests
from typing import Callable, Any

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """
    Decorator for retrying network operations on failure.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    time.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=2.0)
def fetch_url(url: str):
    """
    Simple request wrapper to demonstrate retry logic.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()