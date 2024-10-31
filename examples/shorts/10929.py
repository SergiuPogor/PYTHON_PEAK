import multiprocessing
import time

def compute_square(n):
    time.sleep(1)  # Simulate a time-consuming task
    return n * n

def main():
    numbers = [1, 2, 3, 4, 5]
    
    # Create a pool of worker processes
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(compute_square, numbers)

    print("Results:", results)

if __name__ == "__main__":
    main()