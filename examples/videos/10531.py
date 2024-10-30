import asyncio
import aiohttp

async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()

async def fetch_all(urls: list) -> list:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/users"
    ]

    results = asyncio.run(fetch_all(urls))

    for idx, result in enumerate(results):
        print(f"Result from URL {idx + 1}: {result[:2]}")  # Show first two items for brevity

if __name__ == "__main__":
    main()