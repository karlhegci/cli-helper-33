import re

class ValidationError(Exception):
    pass

def validate_click_interval(interval):
    if not isinstance(interval, (int, float)):
        raise ValidationError('Interval must be a number.')
    if interval <= 0:
        raise ValidationError('Interval must be greater than zero.')

def validate_click_count(count):
    if not isinstance(count, int):
        raise ValidationError('Click count must be an integer.')
    if count < 1:
        raise ValidationError('Click count must be at least 1.')

def validate_configuration(config):
    try:
        validate_click_interval(config.get('click_interval', 0))
        validate_click_count(config.get('click_count', 0))
    except ValidationError as e:
        print(f'Configuration error: {e}')  
        raise

if __name__ == '__main__':
    sample_config = {'click_interval': 0.5, 'click_count': 10}
    try:
        validate_configuration(sample_config)
        print('Configuration is valid.')
    except ValidationError:
        print('Invalid configuration detected.')