"""Command output and text data processing utilities for CLI applications."""

import re
from typing import Dict, List, Union


class TextProcessor:
    """Processes and formats raw command-line text and structured data."""

    def __init__(self, strip_ansi: bool = True, default_indent: int = 2) -> None:
        self.strip_ansi = strip_ansi
        self.default_indent = default_indent
        self._ansi_re = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def clean_output(self, text: str) -> str:
        """Remove ANSI escape codes and normalize whitespace from string.

        Args:
            text: Raw text containing potential ANSI sequences.

        Returns:
            Cleaned string with ANSI sequences stripped.
        """
        if self.strip_ansi:
            text = self._ansi_re.sub("", text)
        return text.strip()

    def format_key_value(
        self,
        data: Dict[str, Union[str, int, float, bool]],
        indent_level: int = 1
    ) -> str:
        """Format a dictionary into aligned key-value pairs for terminal display.

        Args:
            data: Key-value dictionary to format.
            indent_level: Multiplier for default indentation depth.

        Returns:
            Formatted multi-line string representing the data.
        """
        if not data:
            return ""

        indent = " " * (self.default_indent * indent_level)
        max_key_len = max(len(str(k)) for k in data.keys())
        lines: List[str] = []

        for key, val in data.items():
            padded_key = str(key).ljust(max_key_len)
            lines.append(f"{indent}{padded_key} : {val}")

        return "\n".join(lines)

    def truncate(self, text: str, max_length: int = 80, suffix: str = "...") -> str:
        """Truncate text to a maximum length while appending a suffix.

        Args:
            text: Text to be truncated.
            max_length: Maximum allowed output string length.
            suffix: String appended when truncation occurs.

        Returns:
            Truncated string or original text if within limit.
        """
        cleaned = self.clean_output(text)
        if len(cleaned) <= max_length:
            return cleaned

        cutoff = max(0, max_length - len(suffix))
        return cleaned[:cutoff] + suffix
