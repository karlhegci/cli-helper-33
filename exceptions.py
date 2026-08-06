class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class ValidationError(CustomError):
    """Raised for validation errors."""
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(self.message)

class ConnectionError(CustomError):
    """Raised for connection errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def raise_if_invalid(value, field_name):
    if not isinstance(value, str) or not value:
        raise ValidationError("Invalid value provided", field_name)

def perform_operation(data):
    try:
        raise_if_invalid(data.get('name'), 'name')
        # Simulate operation
        print("Operation performed successfully")
    except ValidationError as ve:
        print(f'ValidationError: {ve.message} for field {ve.field}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')