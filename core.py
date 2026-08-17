import time
import pyautogui

class AutoClicker:
    def __init__(self, interval: float):
        self.interval = interval
        self.running = False

    def start_clicking(self):
        self.running = True
        print('AutoClicker started. Press Ctrl+C to stop.')
        try:
            while self.running:
                pyautogui.click()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            self.stop_clicking()

    def stop_clicking(self):
        self.running = False
        print('AutoClicker stopped.')

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.1)  # Adjust interval as needed
    clicker.start_clicking()