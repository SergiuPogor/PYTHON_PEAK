# This script demonstrates how to use shutil.disk_usage
# to monitor disk space in a specified directory.

import shutil
import os

def check_disk_usage(path):
    # Get disk usage statistics
    total, used, free = shutil.disk_usage(path)
    
    # Convert bytes to gigabytes
    total_gb = total // (2**30)
    used_gb = used // (2**30)
    free_gb = free // (2**30)
    
    print(f"Disk Usage for '{path}':")
    print(f"Total: {total_gb} GB")
    print(f"Used: {used_gb} GB")
    print(f"Free: {free_gb} GB")
    
    # Check if disk space is low
    if free < 2 * (2**30):  # Less than 2GB
        print("Warning: Low disk space!")

def main():
    # Specify the path to check
    path = os.path.expanduser("~")  # User's home directory
    check_disk_usage(path)

if __name__ == "__main__":
    main()