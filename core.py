import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval  # Time between clicks
        self.running = False  # Flag to control the clicking loop
        self.thread = None  # Thread for running the clicker

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._click_loop)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()  # Wait for clicker thread to finish

    def _click_loop(self):
        while self.running:
            self._click()
            time.sleep(self.interval)

    @staticmethod
    def _click():
        # Here we would implement the actual click event. For example:
        # pyautogui.click()
        print("Click!")  # Simulated click event

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    clicker.start()
    time.sleep(2)  # Click for 2 seconds
    clicker.stop()
    print("AutoClicker stopped.")