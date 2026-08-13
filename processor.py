import time
import random
from validators import validate_click_settings

class AutoClicker:
    def __init__(self, click_settings):
        self.click_settings = click_settings

    def start_clicking(self):
        click_interval = self.click_settings['interval']
        click_count = self.click_settings['count']
        print('Starting auto-clicker...')
        for _ in range(click_count):
            self.perform_click()
            time.sleep(click_interval)
        print('Finished clicking.')

    def perform_click(self):
        # Simulate a click action (in a real application, this would use an external library)
        print('Click!')

if __name__ == '__main__':
    user_input = {'interval': 0.5, 'count': 10}  # Sample user input
    # Validate user input
    if validate_click_settings(user_input):
        clicker = AutoClicker(user_input)
        clicker.start_clicking()
    else:
        print('Invalid click settings provided.')
