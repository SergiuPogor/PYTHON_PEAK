import time
from functools import wraps

def rate_limiter(max_calls, period):
    def decorator(func):
        last_called = [0.0]  # Store the time of the last call

        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            elapsed = current_time - last_called[0]

            if elapsed < period:
                wait_time = period - elapsed
                print(f"Rate limit exceeded. Please wait {wait_time:.2f} seconds.")
                time.sleep(wait_time)

            last_called[0] = time.time()
            return func(*args, **kwargs)

        return wrapper
    return decorator

@rate_limiter(max_calls=1, period=2)  # Limit to 1 call every 2 seconds
def say_hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(say_hello("Alice"))  # Should print immediately
    print(say_hello("Bob"))    # Should wait for 2 seconds before printing