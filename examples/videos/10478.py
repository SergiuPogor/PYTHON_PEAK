import time
from functools import wraps
import requests

# Throttle decorator to limit API calls
def throttle(rate_limit, per_seconds):
    def decorator(func):
        last_called = [0.0]

        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = per_seconds - elapsed

            if wait_time > 0:
                time.sleep(wait_time)

            last_called[0] = time.time()
            return func(*args, **kwargs)

        return wrapper

    return decorator

# Example API call function with throttle applied
@throttle(rate_limit=5, per_seconds=1)
def fetch_data(url):
    response = requests.get(url)
    return response.json()

# Simulating multiple API calls
def main():
    url = "https://api.example.com/data"
    for _ in range(10):  # Attempting to make 10 API calls
        data = fetch_data(url)
        print(data)

# Uncomment to run the main function
# if __name__ == "__main__":
#     main()