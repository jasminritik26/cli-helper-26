import difflib
from functools import lru_cache
from typing import List, Dict, Optional

class CommandRegistry:
    """Manages registered CLI commands with optimized resolution."""

    def __init__(self) -> None:
        self._commands: Dict[str, str] = {}
        self._sorted_commands: List[str] = []

    def register(self, name: str, description: str) -> None:
        """Registers a command and invalidates the resolution cache."""
        self._commands[name] = description
        self._sorted_commands = sorted(self._commands.keys())
        self.resolve_command.cache_clear()

    @lru_cache(maxsize=256)
    def resolve_command(self, query: str) -> Optional[str]:
        """Resolves a query to the closest registered command using optimized lookups."""
        if not query:
            return None

        # Fast path: exact match
        if query in self._commands:
            return query

        # Optimized prefix match
        prefix_matches = [cmd for cmd in self._sorted_commands if cmd.startswith(query)]
        if prefix_matches:
            return prefix_matches[0]

        # Fallback to fuzzy match with reasonable threshold
        matches = difflib.get_close_matches(query, self._sorted_commands, n=1, cutoff=0.5)
        return matches[0] if matches else None

    def get_description(self, command: str) -> str:
        """Retrieves description for a resolved command."""
        return self._commands.get(command, "No description available.")

    def bulk_register(self, commands: Dict[str, str]) -> None:
        """Registers multiple commands while minimizing cache invalidation overhead."""
        self._commands.update(commands)
        self._sorted_commands = sorted(self._commands.keys())
        self.resolve_command.cache_clear()
