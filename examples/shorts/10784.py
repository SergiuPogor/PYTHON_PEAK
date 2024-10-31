# Using multiprocessing.Queue for safe data sharing

from multiprocessing import Process, Queue
import time

# Worker function to add data to the queue
def worker(queue, data):
    for item in data:
        print(f"Adding {item} to queue")
        queue.put(item)
        time.sleep(0.5)  # Simulate some work

# Worker function to read data from the queue
def reader(queue):
    while True:
        item = queue.get()
        if item is None:  # Exit signal
            break
        print(f"Processing {item}")

if __name__ == "__main__":
    # Create a Queue
    queue = Queue()

    # Data to be processed
    data = [1, 2, 3, 4, 5]

    # Create worker process to add data
    process_writer = Process(target=worker, args=(queue, data))
    process_reader = Process(target=reader, args=(queue,))

    # Start processes
    process_reader.start()
    process_writer.start()

    # Wait for the writer to finish
    process_writer.join()

    # Send exit signal to reader
    queue.put(None)

    # Wait for the reader to finish
    process_reader.join()