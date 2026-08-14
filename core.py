import time
import random

class AutoClicker:
    def __init__(self, clicks_per_second, duration):
        self.clicks_per_second = clicks_per_second
        self.duration = duration

    def validate_input(self):
        if not isinstance(self.clicks_per_second, (int, float)) or self.clicks_per_second <= 0:
            raise ValueError("Clicks per second must be a positive number.")
        if not isinstance(self.duration, (int, float)) or self.duration <= 0:
            raise ValueError("Duration must be a positive number.")

    def start_clicking(self):
        self.validate_input()
        end_time = time.time() + self.duration
        while time.time() < end_time:
            self.perform_click()
            time.sleep(1 / self.clicks_per_second)

    def perform_click(self):
        # Here we would simulate a click. In a real scenario, we might need additional libraries like pyautogui.
        print("Click!")

if __name__ == '__main__':
    clicker = AutoClicker(clicks_per_second=5, duration=10)
    clicker.start_clicking()