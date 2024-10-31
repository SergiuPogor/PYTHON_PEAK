import time
import requests
from functools import wraps

def retry_request(max_retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    if attempt < max_retries - 1:
                        time.sleep(delay)
                        print(f"Retrying... (Attempt {attempt + 2})")
                    else:
                        print("Max retries reached. Request failed.")
                        raise e
        return wrapper
    return decorator

@retry_request(max_retries=5, delay=1)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def main():
    url = "https://api.example.com/data"
    try:
        data = fetch_data(url)
        print(data)
    except Exception as e:
        print(f"Failed to fetch data: {e}")

if __name__ == "__main__":
    main()