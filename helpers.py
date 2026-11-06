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
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    attempts += 1
                    if attempts >= max_retries:
                        raise e
                    time.sleep(delay * (2 ** (attempts - 1)))
            return None
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=2.0)
def fetch_url(url: str):
    """
    Example network operation using retry logic.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()