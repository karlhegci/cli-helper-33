class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class NotFoundError(CustomError):
    """Exception raised for not found errors."""
    def __init__(self, message="Resource not found."):
        self.message = message
        super().__init__(self.message)

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)

class DatabaseError(CustomError):
    """Exception raised for database related errors."""
    def __init__(self, message="Database operation failed."):
        self.message = message
        super().__init__(self.message)

class AuthenticationError(CustomError):
    """Exception raised for authentication errors."""
    def __init__(self, message="Authentication failed."):
        self.message = message
        super().__init__(self.message)