import time
from threading import Lock

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = 0
        self.lock = Lock()
        self.start_time = time.time()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self.lock:
                current_time = time.time()
                elapsed_time = current_time - self.start_time

                # Reset the count if the period has passed
                if elapsed_time > self.period:
                    self.calls = 0
                    self.start_time = current_time

                # Check if the limit has been reached
                if self.calls < self.max_calls:
                    self.calls += 1
                    return func(*args, **kwargs)
                else:
                    raise Exception("Rate limit exceeded. Try again later.")
        return wrapper

@RateLimiter(max_calls=5, period=10)
def api_call(data):
    print(f"API called with data: {data}")

def main():
    for i in range(10):
        try:
            api_call(f"request {i}")
        except Exception as e:
            print(e)
        time.sleep(1)  # Simulating time between calls

if __name__ == "__main__":
    main()