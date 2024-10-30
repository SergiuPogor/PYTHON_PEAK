from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the LRU cache with a specific capacity
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # If the key exists, move it to the end to show it's been recently used
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        # If the key does not exist, return -1
        return -1

    def put(self, key: int, value: int) -> None:
        # If the key exists, update the value and move it to the end
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        # If the cache exceeds capacity, pop the first item (least recently used)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Example Usage:
cache = LRUCache(3)

# Insert key-value pairs into the cache
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)

# Accessing keys to change their usage order
print(f"Get key 1: {cache.get(1)}")  # Output: 1
cache.put(4, 4)  # This will remove key 2 (least recently used)

print(f"Get key 2: {cache.get(2)}")  # Output: -1 (since key 2 was evicted)
print(f"Get key 3: {cache.get(3)}")  # Output: 3
print(f"Get key 4: {cache.get(4)}")  # Output: 4

# Let's see the current cache state:
print("Cache contents:", cache.cache)  # Output: OrderedDict([(1, 1), (3, 3), (4, 4)])

# Advanced Case: Using LRU Cache for caching file processing results
def expensive_file_processing(file_path: str) -> str:
    # Simulate reading from a large file and processing
    with open(file_path, 'r') as file:
        data = file.read()
    return data[:100]  # Simulate returning only part of the file for demonstration

file_cache = LRUCache(2)

# Process and cache file contents
file1_path = '/tmp/test/input1.txt'
file2_path = '/tmp/test/input2.txt'
file_cache.put(file1_path, expensive_file_processing(file1_path))
file_cache.put(file2_path, expensive_file_processing(file2_path))

# Access cached data for file1
print(f"Cached file1 content: {file_cache.get(file1_path)}")

# Adding another file will evict the least recently used file from cache
file3_path = '/tmp/test/input3.txt'
file_cache.put(file3_path, expensive_file_processing(file3_path))

# Check cache status after adding file3
print("Cache after adding file3:", file_cache.cache)  # Output: OrderedDict([(file2_path, ...), (file3_path, ...)])

# File1 content will now be evicted, as it's least recently used
print(f"Cached file1 content after eviction: {file_cache.get(file1_path)}")  # Output: -1