import functools
import re
from typing import Dict, Generator, List, Optional


class CoreCommandProcessor:
    """Core processor for managing, filtering, and caching CLI commands."""

    def __init__(self, commands: List[Dict[str, str]]) -> None:
        # Store commands as an immutable tuple of tuples to support caching mechanisms
        self._commands = tuple(
            (cmd.get("name", ""), cmd.get("usage", ""), cmd.get("description", ""))
            for cmd in commands
        )
        self._compiled_regexes: Dict[str, re.Pattern] = {}

    def _get_compiled_regex(self, pattern: str) -> re.Pattern:
        """Retrieve from local cache or compile and store a new regex pattern."""
        if pattern not in self._compiled_regexes:
            self._compiled_regexes[pattern] = re.compile(pattern, re.IGNORECASE)
        return self._compiled_regexes[pattern]

    @functools.lru_cache(maxsize=128)
    def search_commands(self, query: str) -> List[Dict[str, str]]:
        """Fast cached lookup of commands matching a search query."""
        if not query:
            return [
                {"name": name, "usage": usage, "description": desc}
                for name, usage, desc in self._commands
            ]

        compiled = self._get_compiled_regex(re.escape(query))
        results = []

        for name, usage, desc in self._commands:
            if compiled.search(name) or compiled.search(desc):
                results.append(
                    {"name": name, "usage": usage, "description": desc}
                )

        return results

    def batch_process_stream(
        self, patterns: List[str]
    ) -> Generator[Dict[str, str], None, None]:
        """Memory-efficient generator for filtering commands by multiple patterns."""
        compiled_patterns = [self._get_compiled_regex(p) for p in patterns]

        for name, usage, desc in self._commands:
            if any(pat.search(name) or pat.search(desc) for pat in compiled_patterns):
                yield {"name": name, "usage": usage, "description": desc}
