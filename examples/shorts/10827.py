# Example comparing asyncio.gather() and asyncio.wait()

import asyncio

async def fetch_data(id):
    # Simulate a network call
    await asyncio.sleep(1)
    return f"Data {id}"

async def main():
    # Using asyncio.gather() to fetch multiple tasks
    gather_results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print("Results from gather():", gather_results)

    # Using asyncio.wait() to fetch multiple tasks
    tasks = [
        fetch_data(4),
        fetch_data(5),
        fetch_data(6)
    ]
    done, pending = await asyncio.wait(tasks)
    
    wait_results = [task.result() for task in done]
    print("Results from wait():", wait_results)

# Run the main function
asyncio.run(main())