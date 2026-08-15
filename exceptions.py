class AutoClickerError(Exception):
    """Base class for exceptions in the AutoClicker module."""
    pass

class InvalidConfigurationError(AutoClickerError):
    """Exception raised for invalid configuration errors."""
    def __init__(self, message):
        super().__init__(message)

class ClickRateTooHighError(AutoClickerError):
    """Exception raised when click rate exceeds the limit."""
    def __init__(self, rate):
        message = f'Click rate {rate} exceeds the maximum limit.'
        super().__init__(message)

class ClickerStoppedError(AutoClickerError):
    """Exception raised when the clicker is stopped unexpectedly."""
    pass

class ClickerNotRunningError(AutoClickerError):
    """Exception raised when trying to stop a clicker that is not running."""
    def __init__(self, message):
        super().__init__(message)
