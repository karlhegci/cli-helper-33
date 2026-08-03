import re

def is_valid_email(email):
    # Check if the email address is valid using regex
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None


def is_positive_integer(value):
    # Check if the value is a positive integer
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False


def validate_inputs(inputs):
    # Validate a dictionary of inputs
    errors = []

    if 'email' not in inputs or not is_valid_email(inputs['email']):
        errors.append('Invalid email address')
    
    if 'age' not in inputs or not is_positive_integer(inputs['age']):
        errors.append('Age must be a positive integer')

    return errors

