import functools
from typing import Any, Dict, List, Optional

class CoreModule:
    """Core functionality for cli-helper-26 with performance optimizations."""

    def __init__(self) -> None:
        self._cache: Dict[str, Any] = {}
        self._stats: Dict[str, int] = {"calls": 0, "hits": 0}

    @functools.lru_cache(maxsize=512)
    def _heavy_computation(self, data: str) -> int:
        """Perform heavy computation with automatic caching for performance."""
        # Simulate CPU intensive task
        result = 0
        for i in range(5000):
            result += (i * hash(data)) % 1000
        return result

    def process_data(self, items: List[str]) -> Dict[str, int]:
        """Process list of items with optimized caching."""
        results: Dict[str, int] = {}
        for item in items:
            self._stats["calls"] += 1
            if item in self._cache:
                self._stats["hits"] += 1
                results[item] = self._cache[item]
            else:
                computed = self._heavy_computation(item)
                self._cache[item] = computed
                results[item] = computed
        return results

    def batch_process(self, items: List[str]) -> List[int]:
        """Optimized batch processing using list comprehension."""
        # Leverages lru_cache for repeated items in batch
        return [self._heavy_computation(item) for item in items]

    def get_performance_stats(self) -> Dict[str, Any]:
        """Retrieve performance metrics."""
        cache_info = self._heavy_computation.cache_info()
        return {
            "manual_cache_size": len(self._cache),
            "lru_cache_hits": cache_info.hits,
            "lru_cache_misses": cache_info.misses,
            "manual_hits": self._stats["hits"],
            "total_calls": self._stats["calls"]
        }

def execute_core_task(task_type: str, data: Optional[List[str]] = None) -> Dict[str, Any]:
    """Main entry point for core module tasks."""
    if data is None:
        data = []
    core = CoreModule()
    if task_type == "process":
        return {"results": core.process_data(data)}
    elif task_type == "batch":
        return {"results": core.batch_process(data), "stats": core.get_performance_stats()}
    else:
        return {"error": "Invalid task type"}
