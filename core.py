import functools
import time
from typing import Callable, Any

# Cache for expensive computation results
_CACHE = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in _CACHE:
            _CACHE[args] = func(*args)
        return _CACHE[args]
    return wrapper

def batch_process(data: list, chunk_size: int = 100) -> list:
    """Efficient list processing using generator chunks."""
    def chunker(seq, size):
        for i in range(0, len(seq), size):
            yield seq[i:i + size]
    
    results = []
    for chunk in chunker(data, chunk_size):
        # Simulation of heavy processing logic
        results.extend([x * 2 for x in chunk])
    return results

@memoize
def heavy_computation(n: int) -> int:
    """Simulated heavy computation for demonstration."""
    time.sleep(1)
    return n * n

def run_optimization_pipeline(items: list) -> list:
    """Pipeline runner for optimized data processing."""
    processed = batch_process(items)
    return [heavy_computation(i) for i in processed[:5]]