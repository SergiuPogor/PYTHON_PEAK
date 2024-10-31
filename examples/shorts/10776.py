import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Example usage
def create_singleton_instance(value):
    singleton = Singleton(value)
    print(f'Singleton value: {singleton.value}')

# Create threads to demonstrate thread-safe singleton
thread1 = threading.Thread(target=create_singleton_instance, args=("First",))
thread2 = threading.Thread(target=create_singleton_instance, args=("Second",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()