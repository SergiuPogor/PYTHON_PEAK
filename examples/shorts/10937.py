import threading
import time

class SharedResource:
    def __init__(self):
        self.condition = threading.Condition()
        self.value = 0

    def modify(self, new_value):
        with self.condition:
            self.value = new_value
            print(f"Value updated to: {self.value}")
            self.condition.notify_all()  # Notify waiting threads

    def wait_for_value(self, expected_value):
        with self.condition:
            while self.value < expected_value:
                print(f"Waiting for value to reach {expected_value}...")
                self.condition.wait()  # Wait until notified

def worker(resource, expected_value):
    resource.wait_for_value(expected_value)
    print(f"Worker proceeding with value: {resource.value}")

# Initialize shared resource
shared_resource = SharedResource()

# Create threads
threads = [
    threading.Thread(target=worker, args=(shared_resource, 5)),
    threading.Thread(target=worker, args=(shared_resource, 3))
]

# Start threads
for thread in threads:
    thread.start()

# Simulate some processing before updating the value
time.sleep(2)
shared_resource.modify(3)
time.sleep(2)
shared_resource.modify(5)

# Wait for threads to complete
for thread in threads:
    thread.join()