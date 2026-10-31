import functools
import logging
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger("cli_helper")


def retry_network_op(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    """Decorator to retry network operations with exponential backoff.

    Args:
        max_retries: Maximum number of attempt cycles before failing.
        delay: Initial delay in seconds between retries.
        backoff_factor: Multiplier applied to delay on subsequent attempts.
        exceptions: Exception types to trigger a retry.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            f"Execution failed after {max_retries} attempts: {err}"
                        )
                        raise
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} failed ({err}). "
                        f"Retrying in {current_delay:.1f}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor

        return wrapper

    return decorator
