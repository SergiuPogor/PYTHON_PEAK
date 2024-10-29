import numpy as np
import time

def main():
    # Create a large random dataset
    data_size = 1_000_000
    data = np.random.rand(data_size)

    # Traditional Python loop to compute the square of each element
    start_time = time.time()
    squared_loop = [x ** 2 for x in data]
    print("Loop time: {:.6f} seconds".format(time.time() - start_time))

    # NumPy vectorized operation to compute the square of each element
    start_time = time.time()
    squared_numpy = data ** 2
    print("NumPy time: {:.6f} seconds".format(time.time() - start_time))

    # Check if both results are the same
    print("Results are equal:", np.array_equal(squared_loop, squared_numpy))

if __name__ == "__main__":
    main()