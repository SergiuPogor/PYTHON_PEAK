import threading
import time
import random

class SharedResource:
    def __init__(self):
        self.condition = threading.Condition()
        self.resource = []

    def produce(self):
        while True:
            with self.condition:
                item = random.randint(1, 100)
                self.resource.append(item)
                print(f"Produced: {item}")
                self.condition.notify()  # Notify waiting consumers
            time.sleep(random.uniform(0.5, 2))

    def consume(self):
        while True:
            with self.condition:
                while not self.resource:
                    self.condition.wait()  # Wait for an item to be produced
                item = self.resource.pop(0)
                print(f"Consumed: {item}")

def main():
    shared_resource = SharedResource()

    producer_thread = threading.Thread(target=shared_resource.produce)
    consumer_thread = threading.Thread(target=shared_resource.consume)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    main()