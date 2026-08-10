import requests
import time
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=2):
    """Attempts to send a GET request to the specified URL with retry logic."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()  # Return response as JSON
        except RequestException as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"Failed after {max_retries} attempts: {e}")
                raise

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(f"Error retrieving data: {e}")
