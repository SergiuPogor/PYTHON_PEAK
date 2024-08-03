import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def main():
    # Using aiter() to get an asynchronous iterator
    async_iter = aiter(async_generator())
    
    async for value in async_iter:
        print(value)

asyncio.run(main())

# Another example: Reading lines from an async file object
async def read_file(file_path):
    async with aiofiles.open(file_path, 'r') as file:
        async for line in aiter(file.readline, ''):
            print(line.strip())

# Call the function to read from a file asynchronously
import aiofiles

async def main():
    await read_file('/tmp/test/input.txt')

asyncio.run(main())

# Example: Fetching data from multiple APIs asynchronously
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        for result in aiter(asyncio.as_completed(tasks)):
            print(await result)

urls = [
    "https://api.example.com/data1",
    "https://api.example.com/data2",
    "https://api.example.com/data3"
]

asyncio.run(fetch_all(urls))