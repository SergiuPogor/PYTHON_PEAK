import asyncio
import aiohttp

# Example 1: Using asyncio.gather to make concurrent HTTP requests

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()  # Fetch and return the page content

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)  # Gather all tasks and run them concurrently

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

async def main():
    results = await fetch_all(urls)
    for idx, result in enumerate(results, start=1):
        print(f"Result from URL {idx}: {result[:100]}...")  # Print first 100 characters for brevity

asyncio.run(main())  # Runs the main coroutine and waits for the tasks to complete

# Example 2: Handling errors with asyncio.gather

async def fetch_with_error_handling(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()  # Parse JSON response
            else:
                return {"error": f"Failed to fetch {url}, status code {response.status}"}
    except Exception as e:
        return {"error": f"Error occurred: {str(e)}"}

async def fetch_all_with_error_handling(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_error_handling(session, url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)  # Handle exceptions gracefully

urls_with_error = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://nonexistent-website.com",
    "https://jsonplaceholder.typicode.com/posts/3"
]

async def main_with_error_handling():
    results = await fetch_all_with_error_handling(urls_with_error)
    for idx, result in enumerate(results, start=1):
        if "error" in result:
            print(f"Error for URL {idx}: {result['error']}")
        else:
            print(f"Success for URL {idx}: {result}")

asyncio.run(main_with_error_handling())

# Example 3: Optimizing the number of concurrent requests using semaphores

async def fetch_with_semaphore(sem, session, url):
    async with sem:  # Limit the number of concurrent requests
        async with session.get(url) as response:
            return await response.text()

async def fetch_all_with_limit(urls, limit=2):
    sem = asyncio.Semaphore(limit)  # Only allow 'limit' number of requests at once
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_semaphore(sem, session, url) for url in urls]
        return await asyncio.gather(*tasks)

urls_to_fetch = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4"
]

async def main_with_limit():
    results = await fetch_all_with_limit(urls_to_fetch, limit=2)
    for idx, result in enumerate(results, start=1):
        print(f"Result from URL {idx}: {result[:100]}...")

asyncio.run(main_with_limit())

# Conclusion: asyncio.gather is a powerful tool for handling multiple network requests concurrently in Python.
# Combining it with semaphores or error handling gives you fine control over concurrency and resilience in real-world scenarios.