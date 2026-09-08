import collections
from typing import Any, Callable, Iterable, Iterator, List

class BatchProcessor:
    """Efficiently processes large streams of data in chunks to optimize memory usage and performance."""

    def __init__(self, batch_size: int = 1000):
        if batch_size <= 0:
            raise ValueError("Batch size must be greater than zero.")
        self.batch_size = batch_size

    def _chunk_iterable(self, iterable: Iterable[Any]) -> Iterator[List[Any]]:
        """Splits an iterable into chunks of size batch_size without loading everything into memory."""
        iterator = iter(iterable)
        while True:
            chunk = []
            for _ in range(self.batch_size):
                try:
                    chunk.append(next(iterator))
                except StopIteration:
                    if chunk:
                        yield chunk
                    return
            yield chunk

    def process(self, data_stream: Iterable[Any], transform_func: Callable[[Any], Any]) -> Iterator[Any]:
        """Applies transformation function to data stream using list-comprehension optimized batching."""
        for chunk in self._chunk_iterable(data_stream):
            processed_chunk = [transform_func(item) for item in chunk]
            yield from processed_chunk