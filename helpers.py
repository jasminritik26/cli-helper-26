import functools
import time
import urllib.error
from typing import Any, Callable, Tuple, Type


def retry_network_operation(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (urllib.error.URLError, TimeoutError, ConnectionError),
) -> Callable:
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        raise err
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
            return None
        return wrapper
    return decorator


def fetch_url_data(url: str, timeout: int = 10) -> str:
    """Helper function to safely fetch URL data using retries."""
    import urllib.request
    
    @retry_network_operation(max_retries=3, delay=0.5, backoff_factor=2.0)
    def _execute_request() -> str:
        req = urllib.request.Request(url, headers={"User-Agent": "cli-helper-26/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8")
            
    return _execute_request()
