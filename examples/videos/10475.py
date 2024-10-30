import threading
import time

# Creating an Event object
event = threading.Event()

# Function for the worker thread
def worker():
    print("Worker: Starting work...")
    time.sleep(2)  # Simulate work
    print("Worker: Work done! Notifying main thread.")
    event.set()  # Signal that the work is done

# Function for the main thread
def main():
    print("Main: Starting worker thread.")
    threading.Thread(target=worker).start()  # Start the worker thread
    
    print("Main: Waiting for worker to complete...")
    event.wait()  # Wait until the worker signals
    print("Main: Worker has completed. Proceeding with the rest of the program.")

# Run the main function
if __name__ == "__main__":
    main()