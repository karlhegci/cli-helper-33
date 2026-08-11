import re

class ValidationError(Exception):
    pass

def validate_email(email):
    """
    Validate the email address format.
    """
    if not isinstance(email, str):
        raise ValidationError("Email must be a string.")
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError("Invalid email format.")
    return True

def validate_age(age):
    """
    Validate the age to be a positive integer.
    """
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer.")
    if age < 0:
        raise ValidationError("Age cannot be negative.")
    return True

def validate_username(username):
    """
    Validate the username to be non-empty and alphanumeric.
    """
    if not isinstance(username, str):
        raise ValidationError("Username must be a string.")
    if not username:
        raise ValidationError("Username cannot be empty.")
    if not username.isalnum():
        raise ValidationError("Username must be alphanumeric.")
    return True

# Example usage (commented out to avoid execution):
# validate_email('test@example.com')  # Should pass
# validate_age(25)  # Should pass
# validate_username('user123')  # Should pass
