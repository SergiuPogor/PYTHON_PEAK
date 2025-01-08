import threading
import time

class SharedResource:
    def __init__(self):
        self.data = 0
        self.condition = threading.Condition()

    def update_data(self):
        with self.condition:
            self.data += 1
            print(f"Data updated to: {self.data}")
            # Notify waiting threads that data has changed
            self.condition.notify_all()

    def wait_for_update(self):
        with self.condition:
            # Wait until data is updated
            self.condition.wait()
            print(f"Data accessed: {self.data}")

def producer(shared):
    for _ in range(5):
        time.sleep(1)
        shared.update_data()

def consumer(shared):
    for _ in range(5):
        shared.wait_for_update()

def main():
    shared = SharedResource()
    producer_thread = threading.Thread(target=producer, args=(shared,))
    consumer_thread = threading.Thread(target=consumer, args=(shared,))
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    main()