import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# A simple blocking function to simulate I/O-bound work
def blocking_io():
    time.sleep(2)  # Simulating a delay
    return "Blocking operation completed"

async def main():
    loop = asyncio.get_running_loop()
    
    # Run the blocking function in a separate thread
    with ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, blocking_io)
    
    print(result)

if __name__ == "__main__":
    asyncio.run(main())