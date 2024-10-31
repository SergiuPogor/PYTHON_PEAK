import threading
from concurrent.futures import ThreadPoolExecutor

class ThreadSafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

    def get_count(self):
        with self.lock:
            return self.count

def worker(counter):
    for _ in range(1000):
        counter.increment()

if __name__ == "__main__":
    counter = ThreadSafeCounter()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(5):
            executor.submit(worker, counter)

    print("Final count:", counter.get_count())