import asyncio

async def async_generator():
    for i in range(10):
        await asyncio.sleep(0.1)
        yield i

async def main():
    agen = async_generator()
    
    try:
        while True:
            item = await anext(agen)
            print(f'Got item: {item}')
    except StopAsyncIteration:
        print('All items have been processed')

# Run the main function
asyncio.run(main())
