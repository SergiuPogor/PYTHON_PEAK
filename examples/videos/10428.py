import pdb
import time
import random

# Example of a long-running function that might need debugging mid-execution
def process_data(data_list):
    results = []
    for index, item in enumerate(data_list):
        # Randomly add debug breakpoints
        if item > 80:
            print(f"Debugging large value at index {index}: {item}")
            pdb.set_trace()  # Insert a live breakpoint to examine current data

        results.append(item * 2)  # Example processing step
        time.sleep(0.5)  # Simulate long-running processing

    return results

# Simulate live environment - imagine this function being run in a live system
def live_system_processing():
    data = [random.randint(50, 100) for _ in range(10)]
    print("Starting live data processing...")
    
    # Use try-except with pdb for enhanced debugging during runtime
    try:
        processed_data = process_data(data)
        print("Processing complete. Results:", processed_data)
    except Exception as e:
        print(f"Error encountered: {e}")
        pdb.set_trace()  # Debugging point on error
    
    print("Live processing continues...")

# Call the function to start live debugging
live_system_processing()