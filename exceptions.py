class ClickerError(Exception):
    """Base class for exceptions in the autoclicker module."""
    pass

class InvalidClickFrequencyError(ClickerError):
    """Exception raised for invalid click frequency values."""
    def __init__(self, frequency):
        super().__init__(f"Invalid click frequency: {frequency}. Must be greater than zero.")
        self.frequency = frequency

class ClickerNotActiveError(ClickerError):
    """Exception raised when trying to stop an inactive autoclicker."""
    def __init__(self):
        super().__init__("Cannot stop the autoclicker because it is not currently active.")

class DelayOutOfRangeError(ClickerError):
    """Exception raised for delays outside the permissible range."""
    def __init__(self, delay):
        super().__init__(f"Delay out of range: {delay}. Must be between 0.01 and 10 seconds.")
        self.delay = delay

# Example of raising these exceptions in the code

def set_click_frequency(frequency):
    if frequency <= 0:
        raise InvalidClickFrequencyError(frequency)


def stop_clicker(active):
    if not active:
        raise ClickerNotActiveError()


def set_delay(delay):
    if delay < 0.01 or delay > 10:
        raise DelayOutOfRangeError(delay)