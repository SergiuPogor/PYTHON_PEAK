import shutil

def check_disk_usage(path="/"):
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

if __name__ == "__main__":
    check_disk_usage()  # Check disk usage for root directory