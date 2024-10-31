import weakref

class CachedObject:
    def __init__(self, name):
        self.name = name
        print(f"Creating CachedObject: {self.name}")

    def __del__(self):
        print(f"Deleting CachedObject: {self.name}")

# A simple cache using weak references
class WeakCache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def add(self, key, value):
        self._cache[key] = value

    def get(self, key):
        return self._cache.get(key)

# Example usage
if __name__ == "__main__":
    cache = WeakCache()
    
    # Adding objects to the cache
    obj1 = CachedObject("Object1")
    cache.add("obj1", obj1)

    obj2 = CachedObject("Object2")
    cache.add("obj2", obj2)

    # Accessing objects
    print("Cache contents:")
    print(cache.get("obj1"))
    print(cache.get("obj2"))

    # Deleting the reference to obj1
    del obj1
    print("After deleting obj1 reference:")
    print(cache.get("obj1"))  # Should print None as obj1 is collected
    print(cache.get("obj2"))  # Should still exist