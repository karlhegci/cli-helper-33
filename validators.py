import re


def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.
    Returns True if the email is valid, otherwise False.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validate_phone_number(phone: str) -> bool:
    """
    Validates a phone number to be in the format: (xxx) xxx-xxxx or xxx-xxx-xxxx.
    Returns True if the phone number is valid, otherwise False.
    """
    phone_regex = r'^(\\(?[0-9]{3}\\)?[ ]?[0-9]{3}-[0-9]{4})$'
    return re.match(phone_regex, phone) is not None


def validate_url(url: str) -> bool:
    """
    Validates a URL using a regular expression.
    Returns True if the URL is valid, otherwise False.
    """
    url_regex = r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?$'
    return re.match(url_regex, url) is not None


if __name__ == '__main__':
    # Example usage
    print(validate_email('test@example.com'))  # True
    print(validate_phone_number('(123) 456-7890'))  # True
    print(validate_url('https://www.example.com'))  # True
