import asyncio
import random

# Define the Semaphore limit and a list of tasks
semaphore = asyncio.Semaphore(3)  # Allows only 3 tasks to run concurrently

async def limited_task(task_id):
    async with semaphore:
        # Simulate a network or API call with delay
        delay = random.uniform(0.5, 2.0)
        print(f"Task {task_id} starting with delay {delay:.2f}s")
        await asyncio.sleep(delay)
        print(f"Task {task_id} completed after {delay:.2f}s")

async def main():
    # Schedule multiple tasks, showing control with Semaphore
    tasks = [limited_task(i) for i in range(10)]
    await asyncio.gather(*tasks)

# Execute the main function to observe task limits
asyncio.run(main())