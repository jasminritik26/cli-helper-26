import functools
import re
from typing import Callable, Dict, List, Tuple


class CommandRegistry:
    """Core registry for CLI commands with optimized lookup and caching."""

    def __init__(self) -> None:
        self._commands: Dict[str, Callable] = {}
        self._help_texts: Dict[str, str] = {}
        self._compiled_patterns: Dict[str, re.Pattern] = {}

    def register(self, name: str, help_text: str = "") -> Callable:
        """Decorator to register a CLI command."""
        def decorator(func: Callable) -> Callable:
            self._commands[name] = func
            self._help_texts[name] = help_text
            # Pre-compile regex pattern for accelerated search
            self._compiled_patterns[name] = re.compile(rf".*{re.escape(name)}.*", re.IGNORECASE)
            self.find_matching_commands.cache_clear()
            return func
        return decorator

    @functools.lru_cache(maxsize=256)
    def find_matching_commands(self, query: str) -> List[Tuple[str, str]]:
        """Find commands matching query string using cached pattern searches."""
        clean_query = query.strip()
        if not clean_query:
            return [(name, self._help_texts[name]) for name in self._commands]

        matches = []
        for name, pattern in self._compiled_patterns.items():
            if pattern.search(clean_query):
                matches.append((name, self._help_texts[name]))
        return matches

    def execute(self, name: str, *args, **kwargs):
        """Execute a registered command by name."""
        if name not in self._commands:
            raise KeyError(f"Command '{name}' is not registered.")
        return self._commands[name](*args, **kwargs)

    def clear_cache(self) -> None:
        """Purge the lookup cache manually."""
        self.find_matching_commands.cache_clear()
