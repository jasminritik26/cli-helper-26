import functools
import time
from typing import Any, Callable, Dict

# Cache for performance optimization of expensive operations
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

@memoize
def heavy_computation(data_id: int) -> str:
    """Simulated intensive task with memoization applied."""
    time.sleep(1)
    return f"processed_data_{data_id}"

class DataProcessor:
    """Optimized processor for handling large data sets."""
    def __init__(self) -> None:
        self._results = {}

    def process_batch(self, items: list) -> list:
        """Batch processing utilizing local dictionary lookup."""
        return [self._process_single(i) for i in items]

    def _process_single(self, item: Any) -> Any:
        if item not in self._results:
            self._results[item] = item * 2
        return self._results[item]