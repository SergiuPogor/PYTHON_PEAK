import asyncio

async def fetch_data(id):
    await asyncio.sleep(1)  # Simulate a network call
    return f"Data {id}"

async def main_with_gather():
    # Using asyncio.gather() to run tasks concurrently
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print("Results from gather:", results)

async def main_with_wait():
    tasks = [
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    ]
    # Using asyncio.wait() to run tasks
    done, pending = await asyncio.wait(tasks)
    
    # Collecting results from completed tasks
    results = [task.result() for task in done]
    print("Results from wait:", results)

# Running both main functions
async def run():
    print("Using asyncio.gather()...")
    await main_with_gather()
    
    print("Using asyncio.wait()...")
    await main_with_wait()

asyncio.run(run())