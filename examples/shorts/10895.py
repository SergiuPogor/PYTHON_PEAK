import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls  # Maximum calls allowed
        self.period = period  # Time period in seconds
        self.calls = deque()  # Store timestamps of calls

    def is_allowed(self):
        current_time = time.time()  # Get current time
        # Remove timestamps older than the period
        while self.calls and self.calls[0] < current_time - self.period:
            self.calls.popleft()
        
        # Check if the call is allowed
        if len(self.calls) < self.max_calls:
            self.calls.append(current_time)  # Add new call timestamp
            return True
        return False

# Example function to be rate-limited
def make_request():
    print("Request made at:", time.time())

# Using the RateLimiter
if __name__ == "__main__":
    limiter = RateLimiter(max_calls=5, period=10)  # 5 calls per 10 seconds

    for i in range(10):
        if limiter.is_allowed():
            make_request()
        else:
            print("Rate limit exceeded, try again later.")
        time.sleep(1)  # Wait before the next request