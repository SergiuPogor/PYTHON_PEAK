import asyncio
import random

async def fetch_data(id):
    await asyncio.sleep(random.uniform(0.1, 1))  # Simulating an I/O operation
    return f"Data {id} fetched"

async def process_data(id):
    await asyncio.sleep(random.uniform(0.1, 1))  # Simulating data processing
    return f"Data {id} processed"

async def main():
    ids = range(1, 6)  # Example IDs to process
    fetch_tasks = [fetch_data(id) for id in ids]
    process_tasks = [process_data(id) for id in ids]

    # Using asyncio.gather to run tasks concurrently
    fetched_data = await asyncio.gather(*fetch_tasks)
    processed_data = await asyncio.gather(*process_tasks)

    # Output results
    for data in fetched_data:
        print(data)
    for data in processed_data:
        print(data)

if __name__ == '__main__':
    asyncio.run(main())