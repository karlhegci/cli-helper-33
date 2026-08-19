import time
import random

class AutoClicker:
    def __init__(self, click_interval, click_count):
        self.click_interval = click_interval
        self.click_count = click_count

    def validate_input(self):
        if not isinstance(self.click_interval, (int, float)) or self.click_interval <= 0:
            raise ValueError('Click interval must be a positive number.')
        if not isinstance(self.click_count, int) or self.click_count <= 0:
            raise ValueError('Click count must be a positive integer.')

    def start_clicking(self):
        self.validate_input()
        for _ in range(self.click_count):
            print('Click!')
            time.sleep(self.click_interval)

if __name__ == '__main__':
    try:
        click_interval = float(input('Enter click interval (in seconds): '))
        click_count = int(input('Enter number of clicks: '))
        autoclicker = AutoClicker(click_interval, click_count)
        autoclicker.start_clicking()
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')