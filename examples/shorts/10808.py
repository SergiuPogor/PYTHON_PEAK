import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.value = value
            self.initialized = True

def singleton_usage():
    singleton1 = ThreadSafeSingleton("First Instance")
    singleton2 = ThreadSafeSingleton("Second Instance")

    print(f"Singleton 1 Value: {singleton1.value}")
    print(f"Singleton 2 Value: {singleton2.value}")
    print(f"Are both instances equal? {singleton1 is singleton2}")

singleton_usage()