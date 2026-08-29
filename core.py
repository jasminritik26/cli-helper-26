import functools
from typing import Any, Callable, Dict, List


class CoreProcessor:
    """Core processor for CLI helper with performance optimizations."""

    def __init__(self) -> None:
        self.command_registry: Dict[str, Callable[[List[str], str], Any]] = {}
        # LRU cache applied via decorator for performance

    def register_command(self, name: str, func: Callable) -> None:
        """Register a new command with its handler function."""
        self.command_registry[name] = func

    @functools.lru_cache(maxsize=256)
    def _cached_process(self, input_data: str) -> str:
        """Cached processing for performance on repeated inputs."""
        # Simulate or perform actual processing
        processed = input_data.strip().lower()
        # Additional work to justify cache
        for i in range(500):
            processed = processed + str(i % 10)
            if len(processed) > 100:
                processed = processed[:50]
        return processed[::-1]

    def execute_command(self, command: str, args: List[str]) -> Any:
        """Execute a command using optimized dispatch and caching."""
        if command not in self.command_registry:
            return {"error": f"Command '{command}' not found"}

        # Build key for potential cache use
        arg_str = " ".join(args)
        cached = self._cached_process(arg_str)

        handler = self.command_registry[command]
        # Pass cached result for use in handler
        return handler(args, cached)

    def process_input(self, user_input: str) -> str:
        """Process user CLI input with efficient parsing."""
        if not user_input or not user_input.strip():
            return "Empty input received"

        parts = user_input.strip().split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1].split() if len(parts) > 1 else []

        result = self.execute_command(command, args)
        if isinstance(result, dict):
            return result.get("error", str(result))
        return str(result)


def create_default_processor() -> CoreProcessor:
    """Factory to create processor with sample commands."""
    processor = CoreProcessor()

    def sample_handler(args: List[str], cached: str) -> str:
        """Sample command handler demonstrating cache usage."""
        return f"Processed args: {args} with cache: {cached[:20]}..."

    processor.register_command("sample", sample_handler)
    processor.register_command("help", lambda a, c: "Available: sample, help")
    return processor


if __name__ == "__main__":
    proc = create_default_processor()
    print(proc.process_input("sample test input"))
    print(proc.process_input("help"))
    # Repeated call to show cache
    print(proc.process_input("sample test input"))
