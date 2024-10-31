import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return responses

if __name__ == "__main__":
    urls = [
        'https://example.com',
        'https://jsonplaceholder.typicode.com/posts',
        'https://httpbin.org/get'
    ]
    results = asyncio.run(main(urls))
    for result in results:
        print(result[:100])  # Print the first 100 characters of each response