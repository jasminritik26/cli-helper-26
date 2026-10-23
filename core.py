import functools
import re
from typing import Any, Callable, Dict, Optional, Tuple


class CommandRunner:
    """Core command runner with argument caching and pre-compiled regex pattern matching."""

    def __init__(self) -> None:
        self._registry: Dict[str, Callable[..., Any]] = {}
        # Pre-compile argument parsing pattern for speed across repeated executions
        self._arg_pattern = re.compile(r'(?:[^\s"]|"[^"]*")+')

    def register(self, name: str, func: Callable[..., Any]) -> None:
        """Register a named command handler."""
        self._registry[name] = func

    @functools.lru_cache(maxsize=512)
    def parse_args(self, raw_input: str) -> Tuple[str, ...]:
        """Parse and sanitize CLI input with LRU caching for frequent commands."""
        cleaned = raw_input.strip()
        if not cleaned:
            return ()
        matches = self._arg_pattern.findall(cleaned)
        return tuple(match.strip('"') for match in matches)

    def execute(self, raw_input: str) -> Optional[Any]:
        """Fast-path execution of commands from cached input tokens."""
        tokens = self.parse_args(raw_input)
        if not tokens:
            return None

        cmd_name, *args = tokens
        handler = self._registry.get(cmd_name)
        if not handler:
            raise ValueError(f"Unknown command: {cmd_name}")

        return handler(*args)

    def clear_cache(self) -> None:
        """Purge argument parsing cache."""
        self.parse_args.cache_clear()
