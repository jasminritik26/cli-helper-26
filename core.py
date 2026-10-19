import functools
import concurrent.futures
from typing import List, Tuple, Any


class CoreEngine:
    """Core execution engine with cached lookup and parallel processing."""

    def __init__(self, max_workers: int = 4, cache_size: int = 128) -> None:
        self.max_workers = max_workers
        # Wrap internal compute method with LRU cache to optimize repeat lookups
        self._cached_compute = functools.lru_cache(maxsize=cache_size)(self._compute)

    @staticmethod
    def _compute(task_name: str, payload_tuple: Tuple[Any, ...]) -> str:
        """Simulate core task computation and string transformation."""
        formatted = [str(item).strip().lower() for item in payload_tuple]
        return f"[{task_name.upper()}] -> {':'.join(formatted)}"

    def run_task(self, task_name: str, *payload: Any) -> str:
        """Executes a single task utilizing internal memoization."""
        return self._cached_compute(task_name, payload)

    def run_batch(self, task_list: List[Tuple[str, Tuple[Any, ...]]]) -> List[str]:
        """Executes a batch of core tasks concurrently using thread workers."""
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self.run_task, task_name, *args)
                for task_name, args in task_list
            ]
            return [f.result() for f in concurrent.futures.as_completed(futures)]

    def get_cache_info(self) -> dict:
        """Returns LRU cache statistics for performance monitoring."""
        info = self._cached_compute.cache_info()
        return {
            "hits": info.hits,
            "misses": info.misses,
            "maxsize": info.maxsize,
            "currsize": info.currsize,
        }
