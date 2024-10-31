import asyncio
import aiohttp
import time

# URLs to fetch data from, as if requesting large datasets from different APIs
URLS = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/users"
]

# Async function to fetch data from a single API endpoint
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

# Main function to optimize API calls by fetching all data concurrently
async def fetch_all_data(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

# Entry point to measure how long concurrent API calls take
async def main():
    start_time = time.time()
    data = await fetch_all_data(URLS)
    end_time = time.time()
    print(f"Fetched data from {len(URLS)} APIs in {end_time - start_time:.2f} seconds")

# Run the main function
asyncio.run(main())