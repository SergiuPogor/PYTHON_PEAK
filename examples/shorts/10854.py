import functools

# Function to simulate a time-consuming calculation
@functools.cache
def expensive_function(n):
    # Simulating a delay for the expensive computation
    result = sum(i * i for i in range(n))
    return result

if __name__ == "__main__":
    # Example usage of the caching function
    print(expensive_function(10000))  # Calculates and caches the result
    print(expensive_function(10000))  # Retrieves from cache, much faster
    print(expensive_function(20000))  # New calculation, caches the result