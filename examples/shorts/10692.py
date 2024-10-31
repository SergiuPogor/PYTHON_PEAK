import asyncio
import random

async def fetch_data(id):
    await asyncio.sleep(random.uniform(0.1, 1.0))  # Simulate I/O operation
    return f"Data from task {id}"

async def main():
    tasks = [fetch_data(i) for i in range(5)]
    
    # Running tasks concurrently
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)

# Running the main function
asyncio.run(main())