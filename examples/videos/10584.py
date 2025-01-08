import pandas as pd

# Define the CSV file path
file_path = '/tmp/test/large_dataset.csv'

# Chunk size (number of rows per chunk to read)
chunk_size = 50000  

# Process data in chunks to avoid memory overload
def process_chunk(chunk):
    # Example processing: Count non-null values in 'column_a'
    print("Processing chunk...")
    non_null_count = chunk['column_a'].notnull().sum()
    print(f"Non-null count in 'column_a': {non_null_count}")
    return non_null_count

# Initialize variable for aggregate result
total_non_null_count = 0

# Reading the large CSV in chunks
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Process each chunk and update the aggregate count
    total_non_null_count += process_chunk(chunk)

# Final result
print(f"Total non-null count in 'column_a': {total_non_null_count}")

# Async chunk reading for large files using aiofiles and pandas with asynchronous processing
import asyncio
import aiofiles
from aiofiles import os as async_os

async def async_process_csv_chunk(file_path, chunk_size=50000):
    async with aiofiles.open(file_path, mode='r') as f:
        header = await f.readline()  # Read header separately
        while True:
            lines = [header] + [await f.readline() for _ in range(chunk_size) if not f.at_eof()]
            if not lines:
                break
            chunk = pd.DataFrame([line.strip().split(',') for line in lines[1:]], columns=header.strip().split(','))
            # Example async processing: sum up 'column_a'
            print("Async processing chunk...")
            chunk_sum = chunk['column_a'].astype(float).sum()
            print(f"Chunk sum for 'column_a': {chunk_sum}")

# Run the async CSV processing
asyncio.run(async_process_csv_chunk(file_path))