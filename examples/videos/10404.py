import multiprocessing
import time

# A simple function to simulate a long-running task
def square(n):
    time.sleep(1)  # Simulate a delay
    return n * n

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Using Pool to manage multiple processes
    with multiprocessing.Pool(processes=4) as pool:
        # Map the function to the list of numbers
        results = pool.map(square, numbers)

    print("Squares:", results)

if __name__ == "__main__":
    main()