import functools
import time
import logging

# Configure logger for core operations
logger = logging.getLogger('cli-helper-26.handler')

# Cache dictionary for memoization of expensive calls
_result_cache = {}

def memoize_handler(func):
    """Decorator to cache results of repetitive handler tasks."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _result_cache:
            _result_cache[key] = func(*args, **kwargs)
        return _result_cache[key]
    return wrapper

@memoize_handler
def execute_task(task_id: int, intensity: int) -> str:
    """Simulates a heavy computational task with caching."""
    # Simulating load
    time.sleep(0.5)
    return f"result_from_{task_id}_with_intensity_{intensity}"

class TaskHandler:
    """Main handler for processing CLI commands efficiently."""
    def __init__(self):
        self.processed_count = 0

    def run_batch(self, task_list: list) -> list:
        """Process a list of tasks using optimized lookups."""
        results = []
        for task in task_list:
            start = time.perf_counter()
            res = execute_task(task.get('id'), task.get('level', 1))
            duration = time.perf_counter() - start
            
            logger.debug(f"Task {task.get('id')} completed in {duration:.4f}s")
            results.append(res)
            self.processed_count += 1
        return results