import asyncio

# Simulated async function that might raise an exception
async def fetch_data(source):
    if source == "unreliable":
        raise ValueError("Data source is unreliable!")
    await asyncio.sleep(1)  # Simulate network delay
    return f"Data from {source}"

# Async function to handle exceptions individually within gather
async def process_data_sources(sources):
    tasks = [asyncio.create_task(fetch_data(source)) for source in sources]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Process each result, including exceptions
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Error in source {sources[i]}: {result}")
        else:
            print(f"Success: {result}")

# Using a custom async error handler for robust exception handling
async def robust_fetch(source):
    try:
        result = await fetch_data(source)
        print(f"Fetched successfully: {result}")
    except ValueError as e:
        print(f"Failed to fetch from {source}: {e}")

async def main():
    sources = ["reliable1", "reliable2", "unreliable", "reliable3"]
    print("Handling exceptions with gather() and return_exceptions=True:")
    await process_data_sources(sources)

    print("\nHandling exceptions individually in separate tasks:")
    tasks = [robust_fetch(source) for source in sources]
    await asyncio.gather(*tasks)

# Run the main event loop
asyncio.run(main())