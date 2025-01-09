from collections import OrderedDict

# Function to demonstrate the use of OrderedDict
def process_data(data):
    ordered_data = OrderedDict()
    
    # Populate OrderedDict
    for key, value in data.items():
        ordered_data[key] = value
    
    # Move an item to the end
    ordered_data.move_to_end('B')
    
    # Print items in order
    for key, value in ordered_data.items():
        print(f"{key}: {value}")

# Sample data to process
data_input = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4
}

# Run the function
process_data(data_input)

# Function to compare performance of dict and OrderedDict
def compare_performance():
    import time

    # Creating a large dataset
    large_data = {str(i): i for i in range(100000)}

    # Measure time for dict
    start_time = time.time()
    normal_dict = {k: v for k, v in large_data.items()}
    elapsed_time_dict = time.time() - start_time

    # Measure time for OrderedDict
    start_time = time.time()
    ordered_dict = OrderedDict((k, v) for k, v in large_data.items())
    elapsed_time_ordered = time.time() - start_time

    print(f"Time for regular dict: {elapsed_time_dict:.6f} seconds")
    print(f"Time for OrderedDict: {elapsed_time_ordered:.6f} seconds")

# Run performance comparison
compare_performance()