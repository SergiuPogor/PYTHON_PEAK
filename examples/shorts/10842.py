class InMemoryCache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key, None)

    def set(self, key, value):
        self.cache[key] = value

    def clear(self):
        self.cache.clear()

# Example of using the InMemoryCache
def fetch_data(key):
    # Simulating a slow data fetching process
    print(f"Fetching data for {key}...")
    return f"Data for {key}"

cache = InMemoryCache()

# Fetch data with caching
def get_cached_data(key):
    # Check if data is already in the cache
    cached_value = cache.get(key)
    if cached_value is not None:
        print("Cache hit!")
        return cached_value
    # If not cached, fetch the data
    data = fetch_data(key)
    cache.set(key, data)  # Store it in cache for next time
    return data

# Test the caching mechanism
print(get_cached_data("user:1"))  # Fetch and cache
print(get_cached_data("user:1"))  # Retrieve from cache