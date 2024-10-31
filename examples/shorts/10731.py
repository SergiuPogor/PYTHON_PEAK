# A generator function to stream large data
def data_stream():
    for i in range(1, 101):  # Simulating a stream of data from 1 to 100
        yield i  # Yield each number one at a time

# Function to process the streamed data
def process_stream():
    for number in data_stream():  # Using the generator
        # Simulate processing of each number
        print(f"Processing number: {number}")

# Run the data streaming process
process_stream()