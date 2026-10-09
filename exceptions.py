class CLIHelperError(Exception):
    """Base exception class for cli-helper-26."""
    pass

class ConfigurationError(CLIHelperError):
    """Raised when configuration settings are invalid."""
    pass

class ProcessingError(CLIHelperError):
    """Raised during core data processing failures."""
    pass

class CacheLookupError(CLIHelperError):
    """Raised when performance cache retrieval fails."""
    pass

# Pre-instantiated exceptions for performance
# Reduces object allocation overhead in hot paths
CACHE_MISS = CacheLookupError("requested resource not in cache")
INVALID_CONFIG = ConfigurationError("provided config object is malformed")

def raise_if_none(value, error_type):
    """Inline-optimized check for null references."""
    if value is None:
        raise error_type