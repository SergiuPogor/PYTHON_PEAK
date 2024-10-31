import asyncio

async def task(name, duration):
    print(f"Task {name} started, will take {duration} seconds.")
    await asyncio.sleep(duration)  # Non-blocking wait
    print(f"Task {name} completed!")

async def main():
    # Starting multiple tasks simultaneously
    await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1)
    )
    print("All tasks completed!")

# Running the main function
if __name__ == "__main__":
    asyncio.run(main())