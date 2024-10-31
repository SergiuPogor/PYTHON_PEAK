import time
from threading import Lock

# Throttle decorator to limit function calls
def throttle(seconds):
    def decorator(func):
        last_called = 0
        lock = Lock()
        
        def wrapper(*args, **kwargs):
            nonlocal last_called
            with lock:
                elapsed = time.time() - last_called
                if elapsed < seconds:
                    time.sleep(seconds - elapsed)
                last_called = time.time()
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# Use-case: limit API call rate to once every 2 seconds
@throttle(2)
def fetch_data(api_endpoint):
    # Simulate an API call (replaced with print for demo)
    print(f"Fetching data from {api_endpoint} at {time.strftime('%X')}")

# Test function call throttling
if __name__ == "__main__":
    api_endpoints = ["https://api1.example.com", "https://api2.example.com", "https://api3.example.com"]
    for endpoint in api_endpoints:
        fetch_data(endpoint)

# Output example:
# Fetching data from https://api1.example.com at 12:01:00
# Fetching data from https://api2.example.com at 12:01:02
# Fetching data from https://api3.example.com at 12:01:04