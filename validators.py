import time
import requests
from requests.exceptions import RequestException

def retry_request(url, retries=3, delay=2):
    """Perform a GET request with retry logic."
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            if attempt < retries - 1:
                print(f"Error occurred: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"Failed after {retries} attempts.")
                raise

# Example usage:
# if __name__ == '__main__':
#     try:
#         data = retry_request('https://api.example.com/data')
#         print(data)
#     except Exception as e:
#         print(f'Unable to retrieve data: {e}')