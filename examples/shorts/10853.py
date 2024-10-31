import multiprocessing
import time

# Function to simulate a time-consuming task
def square(x):
    time.sleep(1)  # Simulate delay
    return x * x

if __name__ == "__main__":
    # Input data
    data = [1, 2, 3, 4, 5]
    
    # Create a Pool with the number of CPU cores available
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Execute tasks in parallel
        results = pool.map(square, data)

    # Display the results
    print(results)  # Output: [1, 4, 9, 16, 25]