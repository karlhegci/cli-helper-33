import time
import requests
from requests.exceptions import RequestException

def retry_request(url, retries=3, delay=2):
    """Send a GET request to the specified URL with retry logic."
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            else:
                raise

# Example usage:
# result = retry_request('https://api.example.com/data')
# print(result)
