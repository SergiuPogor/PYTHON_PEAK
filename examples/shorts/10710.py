import multiprocessing
import time

def square(n):
    time.sleep(1)  # Simulating a time-consuming task
    return n * n

def main():
    numbers = [1, 2, 3, 4, 5]
    
    # Creating a Pool of workers
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(square, numbers)
    
    print(f"Squared results: {results}")

if __name__ == "__main__":
    main()