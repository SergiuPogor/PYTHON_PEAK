import multiprocessing
import time

def process_data(data_chunk):
    # Simulate time-consuming processing
    time.sleep(1)
    return sum(data_chunk)

def main():
    data = [i for i in range(100)]
    chunk_size = 10
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Create a pool of workers
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(process_data, chunks)

    # Combine results
    total_sum = sum(results)
    print(f"Total Sum: {total_sum}")

if __name__ == "__main__":
    main()