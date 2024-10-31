# Code Example: Using asyncio.gather to Run Multiple Tasks Concurrently

import asyncio
import aiohttp

# Function to fetch data from a URL asynchronously
async def fetch_data(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()

# Main function to run multiple fetch tasks concurrently
async def gather_data_from_urls(urls: list[str]) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        # Initiate multiple fetch_data tasks simultaneously
        tasks = [fetch_data(session, url) for url in urls]
        # asyncio.gather runs all tasks at the same time
        return await asyncio.gather(*tasks)

# URLs for testing parallel API calls
urls_to_fetch = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

# Run the asynchronous gathering of data
async def main():
    results = await gather_data_from_urls(urls_to_fetch)
    for i, result in enumerate(results):
        print(f"Result from URL {i + 1}: {result}")

# Entry point for the asyncio event loop
asyncio.run(main())