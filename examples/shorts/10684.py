import shutil

def monitor_disk_space():
    # Get disk usage statistics
    total, used, free = shutil.disk_usage("/")

    # Calculate percentage used
    used_percent = (used / total) * 100

    # Display disk usage statistics
    print("Disk Usage Statistics:")
    print(f"Total: {total // (2**30)} GiB")
    print(f"Used: {used // (2**30)} GiB")
    print(f"Free: {free // (2**30)} GiB")
    print(f"Used Percentage: {used_percent:.2f}%")

    # Warning if disk usage exceeds a threshold
    if used_percent > 80:
        print("Warning: Disk usage is above 80%! Consider cleaning up space.")

# Example usage
monitor_disk_space()

# Example 2: Monitoring specific directory usage
def check_directory_usage(path):
    total, used, free = shutil.disk_usage(path)
    print(f"Directory '{path}' - Total: {total // (2**30)} GiB, "
          f"Used: {used // (2**30)} GiB, Free: {free // (2**30)} GiB")

# Check usage for a specific directory
check_directory_usage("/tmp/test")