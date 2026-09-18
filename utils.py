import functools
import logging
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger("cli_helper.utils")


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.0,
    retryable_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """Decorator to retry network operations with exponential backoff."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = backoff_factor
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retryable_exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            "Execution failed after %d attempts: %s",
                            max_retries,
                            str(err),
                        )
                        raise
                    logger.warning(
                        "Attempt %d/%d failed (%s). Retrying in %.1fs...",
                        attempt,
                        max_retries,
                        err,
                        delay,
                    )
                    time.sleep(delay)
                    delay *= 2.0

        return wrapper

    return decorator
