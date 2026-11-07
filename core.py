import logging
import random
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger("cli_helper")


def retry_network_operation(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """Decorator providing exponential backoff retries for network calls."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as exc:
                    if attempt == max_retries:
                        logger.error("Function '%s' failed after %d retries: %s", func.__name__, max_retries, exc)
                        raise
                    
                    sleep_duration = current_delay
                    if jitter:
                        sleep_duration += random.uniform(0, 0.1 * current_delay)
                    
                    logger.warning(
                        "Attempt %d/%d for '%s' failed (%s). Retrying in %.2fs...",
                        attempt, max_retries, func.__name__, exc, sleep_duration
                    )
                    time.sleep(sleep_duration)
                    current_delay *= backoff_factor
        return wrapper
    return decorator


def execute_with_retry(
    operation: Callable,
    *args: Any,
    max_retries: int = 3,
    delay: float = 1.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    **kwargs: Any
) -> Any:
    """Helper function to execute any callable directly with automatic retry logic."""
    wrapped = retry_network_operation(
        max_retries=max_retries,
        delay=delay,
        retryable_exceptions=exceptions
    )(operation)
    return wrapped(*args, **kwargs)
