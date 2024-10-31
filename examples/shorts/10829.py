import asyncio

# Simulated I/O-bound tasks
async def fetch_data(task_id):
    await asyncio.sleep(2)  # Simulating a network delay
    return f"Data from task {task_id}"

async def main():
    tasks = [fetch_data(i) for i in range(1, 6)]  # Creating 5 tasks
    results = await asyncio.gather(*tasks)  # Running tasks concurrently
    
    for result in results:
        print(result)

# Running the main function
if __name__ == "__main__":
    asyncio.run(main())