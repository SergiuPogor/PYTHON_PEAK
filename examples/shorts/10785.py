# Using asyncio.Semaphore for limiting concurrency

import asyncio
import random

async def fetch_data(semaphore, task_id):
    async with semaphore:  # Limit access to the following block
        print(f"Task {task_id} is fetching data...")
        await asyncio.sleep(random.uniform(0.5, 2))  # Simulate network delay
        print(f"Task {task_id} has completed fetching data.")

async def main():
    num_tasks = 10  # Total number of tasks
    max_concurrent = 3  # Limit of concurrent tasks
    semaphore = asyncio.Semaphore(max_concurrent)

    tasks = [fetch_data(semaphore, i) for i in range(num_tasks)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())