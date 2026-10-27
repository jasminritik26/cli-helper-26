import functools
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Tuple, Type


def retry_network_op(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (
        urllib.error.URLError,
        TimeoutError,
        ConnectionError,
    ),
) -> Callable:
    """Decorator that retries network calls with exponential backoff."""
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
        return wrapper
    return decorator


class NetworkProcessor:
    """Processes network requests for CLI tasks with retry resiliency."""

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    @retry_network_op(max_retries=3, delay=0.5, backoff_factor=2.0)
    def fetch_data(self, url: str) -> str:
        """Fetch text data from a remote URL with retry handling."""
        request = urllib.request.Request(
            url, headers={"User-Agent": "cli-helper-26/1.0"}
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            return response.read().decode("utf-8")
