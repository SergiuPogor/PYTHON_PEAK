import psutil
import time

# Function to monitor memory usage of the current process
def monitor_memory_usage():
    process = psutil.Process()  # Get current process
    while True:  # Infinite loop for continuous monitoring
        mem_info = process.memory_info()  # Get memory info
        memory_usage = mem_info.rss / (1024 * 1024)  # Convert bytes to MB
        print(f"Memory Usage: {memory_usage:.2f} MB")  # Print memory usage
        time.sleep(1)  # Sleep for 1 second before next check

# Call the memory monitoring function
monitor_memory_usage()