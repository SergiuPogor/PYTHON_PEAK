import shutil

def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    print(f"Total disk space: {total // (2**30)} GiB")
    print(f"Used disk space: {used // (2**30)} GiB")
    print(f"Free disk space: {free // (2**30)} GiB")
    
    # Check if free space is less than 10%
    if free / total < 0.1:
        print("Warning: Less than 10% disk space left!")
    else:
        print("Sufficient disk space available.")

if __name__ == "__main__":
    check_disk_space()