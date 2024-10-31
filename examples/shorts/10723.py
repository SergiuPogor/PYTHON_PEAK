import time
from functools import wraps

def rate_limiter(max_calls, period):
    """Decorator to limit the number of calls to a function."""
    def decorator(func):
        calls = 0
        first_call_time = None

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls, first_call_time
            current_time = time.time()

            # Reset the count if the period has passed
            if first_call_time is None or current_time - first_call_time > period:
                first_call_time = current_time
                calls = 1
            else:
                calls += 1

            # Check if the limit is exceeded
            if calls > max_calls:
                wait_time = period - (current_time - first_call_time)
                print(f"Rate limit exceeded. Please wait {wait_time:.2f} seconds.")
                time.sleep(wait_time)
                calls = 1  # Reset the count after waiting

            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# Example usage of the rate limiter
@rate_limiter(max_calls=5, period=10)
def limited_function():
    print("Function called!")

# Simulating multiple calls to test rate limiting
if __name__ == "__main__":
    for _ in range(10):
        limited_function()
        time.sleep(1)  # Wait 1 second between calls