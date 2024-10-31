import threading
import time

# Shared resource
shared_data = []

# Create an Event object
data_ready = threading.Event()

def producer():
    global shared_data
    for i in range(5):
        time.sleep(1)  # Simulate work
        shared_data.append(i)
        print(f"Produced: {i}")
    data_ready.set()  # Signal that data is ready

def consumer():
    data_ready.wait()  # Wait for the producer to signal
    print("Consumer is processing the data:")
    for item in shared_data:
        print(f"Consumed: {item}")

if __name__ == "__main__":
    # Start the producer and consumer threads
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()