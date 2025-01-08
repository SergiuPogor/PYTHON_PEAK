from multiprocessing import Process, Value
import time

# Function that modifies a shared variable
def increment(shared_value: Value, lock):
    for _ in range(100):
        with lock:
            shared_value.value += 1
        time.sleep(0.01)  # Simulating work

# Function that reads the shared variable
def reader(shared_value: Value, lock):
    for _ in range(100):
        with lock:
            print(f"Current Value: {shared_value.value}")
        time.sleep(0.01)  # Simulating work

if __name__ == "__main__":
    # Creating a shared variable of type 'int'
    shared_counter = Value('i', 0)
    lock = Value('i', 0)  # Simple lock for synchronization
    
    # Creating processes
    process_list = []
    for _ in range(5):  # Start 5 incrementing processes
        p = Process(target=increment, args=(shared_counter, lock))
        process_list.append(p)
        p.start()
    
    # Start a reader process
    reader_process = Process(target=reader, args=(shared_counter, lock))
    reader_process.start()
    
    # Wait for all processes to finish
    for p in process_list:
        p.join()
    
    reader_process.join()
    print(f"Final Value: {shared_counter.value}")  # Final output