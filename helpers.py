import functools

import collections

from typing import List, Dict, Any

def get_unique_preserved(items: List[Any]) -> List[Any]:
    """Return list of unique items preserving original order.
    Optimized using a dict for O(1) average lookups instead of O(n) list search.
    """
    seen = {}
    unique = []
    for item in items:
        if item not in seen:
            seen[item] = True
            unique.append(item)
    return unique

def count_frequencies(items: List[Any]) -> Dict[Any, int]:
    """Count frequencies of items in list using Counter.
    This is more efficient than manual loops for counting.
    """
    return dict(collections.Counter(items))

@functools.lru_cache(maxsize=128)
def compute_similarity(text1: str, text2: str) -> float:
    """Compute Jaccard similarity between two texts with caching.
    Caching optimizes for repeated comparisons in core processing.
    """
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    if not words1 and not words2:
        return 1.0
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    return intersection / union if union > 0 else 0.0

def batch_process(data: List[Dict[str, Any]], batch_size: int = 100) -> List[Dict[str, Any]]:
    """Process data in batches for better memory performance.
    Avoids loading entire result set at once for large inputs.
    """
    results: List[Dict[str, Any]] = []
    for i in range(0, len(data), batch_size):
        batch = data[i : i + batch_size]
        # Example processing: filter non-empty
        processed_batch = [item for item in batch if item.get("value") is not None]
        results.extend(processed_batch)
    return results

def filter_exclusions(data: List[Any], exclusions: List[Any]) -> List[Any]:
    """Filter out excluded items using set for O(1) checks.
    Performance optimization for large datasets in core module.
    """
    exclusion_set = set(exclusions)
    return [item for item in data if item not in exclusion_set]

def merge_dicts_efficiently(dicts_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Merge list of dicts efficiently with update.
    Avoids creating many intermediate objects.
    """
    merged: Dict[str, Any] = {}
    for d in dicts_list:
        merged.update(d)
    return merged