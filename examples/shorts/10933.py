from multiprocessing import Process, Value
import time

def increment(shared_counter):
    for _ in range(10):
        time.sleep(0.1)  # Simulate work
        shared_counter.value += 1

def main():
    # Create a shared counter using multiprocessing.Value
    counter = Value('i', 0)  # 'i' for integer
    
    # Create and start a process
    process = Process(target=increment, args=(counter,))
    process.start()
    
    # Wait for the process to finish
    process.join()
    
    # Display the value of the shared counter
    print(f"Final counter value: {counter.value}")

if __name__ == "__main__":
    main()