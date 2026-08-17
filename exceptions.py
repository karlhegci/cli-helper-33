class AutoClickerError(Exception):
    """Base class for exceptions in the AutoClicker application."""
    pass

class ClickRateError(AutoClickerError):
    """Exception raised for invalid click rate errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class ClickLimitExceeded(AutoClickerError):
    """Exception raised when the click limit is exceeded."""
    def __init__(self, limit: int) -> None:
        message = f'Click limit of {limit} exceeded.'
        super().__init__(message)

class ConfigurationError(AutoClickerError):
    """Exception raised for configuration related errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)