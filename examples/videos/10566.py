import multiprocessing
import time
import random

# Function to simulate data production
def producer(queue):
    for _ in range(5):
        item = random.randint(1, 100)
        queue.put(item)
        print(f"Produced: {item}")
        time.sleep(random.random())

# Function to simulate data consumption
def consumer(queue):
    while True:
        item = queue.get()
        if item is None:  # Exit signal
            break
        print(f"Consumed: {item}")
        time.sleep(random.random())

def main():
    # Create a multiprocessing queue
    queue = multiprocessing.Queue()

    # Create producer and consumer processes
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    # Start the processes
    producer_process.start()
    consumer_process.start()

    # Wait for the producer to finish
    producer_process.join()

    # Send exit signal to consumer
    queue.put(None)
    
    # Wait for the consumer to finish
    consumer_process.join()

if __name__ == "__main__":
    main()

# This code demonstrates how to safely share data between processes using multiprocessing.Queue.