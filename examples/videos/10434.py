class SimpleCache:
    def __init__(self):
        # Initialize an empty dictionary to store cached data
        self.cache = {}

    def get(self, key):
        # Return the cached value if it exists
        return self.cache.get(key)

    def set(self, key, value):
        # Store the value in the cache
        self.cache[key] = value

def expensive_operation(n):
    # Simulate a time-consuming computation
    result = 0
    for i in range(n):
        result += i
    return result

def main():
    cache = SimpleCache()
    values_to_calculate = [10000, 20000, 30000]

    for value in values_to_calculate:
        # Check if the result is in the cache
        cached_result = cache.get(value)
        if cached_result is not None:
            print(f"Retrieved from cache: {cached_result} for input: {value}")
        else:
            # Perform the expensive operation and cache the result
            result = expensive_operation(value)
            cache.set(value, result)
            print(f"Computed and cached: {result} for input: {value}")

if __name__ == "__main__":
    main()