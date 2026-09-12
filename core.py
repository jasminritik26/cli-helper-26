import sys
import shutil


def format_header(title: str, character: str = "=") -> str:
    """Format a title string into a centered header block."""
    terminal_width = shutil.get_terminal_size((80, 24)).columns
    padding = max(0, (terminal_width - len(title) - 2) // 2)
    border = character * padding
    return f"{border} {title} {border}"


def confirm_action(prompt: str, default: bool = False) -> bool:
    """Prompt the user for a yes/no confirmation in the CLI."""
    suffix = " [Y/n]: " if default else " [y/N]: "
    user_input = input(f"{prompt}{suffix}").strip().lower()

    if not user_input:
        return default
    return user_input in ("y", "yes")


def print_status(message: str, success: bool = True) -> None:
    """Print a status message with simple color indicators."""
    prefix = "[SUCCESS]" if success else "[FAILED]"
    print(f"{prefix} {message}", file=sys.stdout if success else sys.stderr)


def truncate_text(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """Truncate long text to fit within standard display limits."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix
