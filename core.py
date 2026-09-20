import time
import urllib.request
import urllib.error
from functools import wraps

def retry(max_attempts=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    """
    Decorator that retries a function call with exponential backoff.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        raise e
                    print(f"[Warning] Attempt {attempt}/{max_attempts} failed: {e}. Retrying in {current_delay:.1f}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry(max_attempts=4, delay=1.0, backoff=2.0, exceptions=(urllib.error.URLError, urllib.error.HTTPError))
def fetch_url(url: str, timeout: int = 5) -> str:
    """
    Fetch the content of a URL with built-in retry logic.
    """
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'cli-helper/2.6'}
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode('utf-8')
