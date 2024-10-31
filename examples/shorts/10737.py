import multiprocessing
import time

def process_data(data):
    # Simulating a time-consuming task
    time.sleep(1)  # Sleep for 1 second to mimic a slow function
    return data * 2  # Example operation: doubling the input

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]  # Sample data to process

    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(process_data, data)

    print("Processed Results:", results)  # Output: [2, 4, 6, 8, 10]