from functools import lru_cache

class CLIHelperError(Exception):
    """Base exception for cli-helper-26."""
    pass

class ConfigurationError(CLIHelperError):
    """Raised when config validation fails."""
    pass

@lru_cache(maxsize=128)
def format_error_message(error_code: int, details: str) -> str:
    """
    Cached formatter for recurring error messages to reduce string overhead.
    """
    return f"[Error {error_code}]: {details}"

class PerformanceHandler:
    """
    Optimized handler for managing exception propagation and logging.
    """
    def __init__(self):
        self._cache = {}

    def raise_with_context(self, code: int, message: str) -> None:
        """
        Raises an exception with a pre-formatted message from cache.
        """
        formatted = format_error_message(code, message)
        if code >= 500:
            raise CLIHelperError(formatted)
        raise ConfigurationError(formatted)

# Singleton instance for module-level access
error_handler = PerformanceHandler()