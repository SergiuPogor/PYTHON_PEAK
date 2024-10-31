import time
from functools import wraps
import random

# Decorator to retry a function up to 3 times if it raises an exception
def retry_decorator(retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempts + 1} failed with error: {e}")
                    attempts += 1
                    time.sleep(delay)
            raise Exception(f"All {retries} attempts failed.")
        return wrapper
    return decorator

# Example function that simulates a request that may fail
@retry_decorator(retries=3, delay=2)
def fetch_data():
    # Simulate random failures
    if random.choice([True, False]):
        raise ConnectionError("Failed to connect to server.")
    return "Data fetched successfully!"

# Testing the function with the retry decorator
try:
    print(fetch_data())
except Exception as e:
    print(e)