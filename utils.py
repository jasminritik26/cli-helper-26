"""Utility functions for formatting and interacting with command line interface."""

from typing import Any, Sequence


def format_cli_table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> str:
    """Format tabular data into a readable plain-text CLI table.

    Args:
        headers: Sequence of header column names.
        rows: Sequence of rows containing values for each column.

    Returns:
        Formatted string representation of the table.
    """
    if not headers:
        return ""

    str_rows = [[str(cell) for cell in row] for row in rows]
    col_widths = [
        max(len(header), max((len(row[i]) for row in str_rows if i < len(row)), default=0))
        for i, header in enumerate(headers)
    ]

    row_format = "  ".join(f"{{:<{width}}}" for width in col_widths)
    separator = "  ".join("-" * width for width in col_widths)

    lines = [row_format.format(*headers), separator]
    for row in str_rows:
        padded_row = row + [""] * (len(headers) - len(row))
        lines.append(row_format.format(*padded_row[:len(headers)]))

    return "\n".join(lines)


def confirm_action(prompt: str, default: bool = False) -> bool:
    """Prompt the user for a yes/no confirmation via standard input.

    Args:
        prompt: Question or prompt message to display.
        default: Default boolean choice if input is empty.

    Returns:
        True if the user accepts, False otherwise.
    """
    suffix = " [Y/n] " if default else " [y/N] "
    user_input = input(f"{prompt}{suffix}").strip().lower()

    if not user_input:
        return default
    return user_input in ("y", "yes")


def truncate_text(text: str, max_length: int = 50, ellipsis: str = "...") -> str:
    """Truncate string to maximum specified length with an ellipsis.

    Args:
        text: Input string to be truncated.
        max_length: Maximum allowable length including ellipsis.
        ellipsis: String sequence used to indicate truncation.

    Returns:
        Truncated string or original text if within limit.
    """
    if len(text) <= max_length:
        return text
    if max_length <= len(ellipsis):
        return ellipsis[:max_length]
    return text[: max_length - len(ellipsis)] + ellipsis
