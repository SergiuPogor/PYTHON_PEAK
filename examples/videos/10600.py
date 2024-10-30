import asyncio
import time

async def fetch_data(delay, data_id):
    print(f"Fetching data {data_id}...")
    await asyncio.sleep(delay)
    print(f"Data {data_id} fetched after {delay} seconds")
    return f"Data {data_id}"

async def main():
    # Running multiple tasks concurrently
    tasks = [
        fetch_data(2, 1),
        fetch_data(1, 2),
        fetch_data(3, 3)
    ]
    results = await asyncio.gather(*tasks)
    
    # Process the results
    for result in results:
        print(f"Processed: {result}")

# Measure time taken to run the main function
start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(f"Completed in {end_time - start_time:.2f} seconds")