import threading
import time

# Thread-local storage
thread_local_data = threading.local()

def process_data(data):
    # Each thread gets its own storage
    thread_local_data.value = data
    time.sleep(0.1)  # Simulate processing time
    return thread_local_data.value

def thread_function(name, data):
    result = process_data(data)
    print(f"Thread {name}: {result}")

def main():
    # Sample data for different threads
    thread_data = [10, 20, 30, 40, 50]
    threads = []

    for index, data in enumerate(thread_data):
        thread = threading.Thread(target=thread_function, args=(index, data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

# This code demonstrates how to use thread-local storage
# in Python. Each thread maintains its own copy of the data,
# preventing data corruption or leaks when accessing shared resources.