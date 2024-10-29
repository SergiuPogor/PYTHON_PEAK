import signal
import time

# Function to handle the interrupt signal
def signal_handler(sig, frame):
    print("\nGracefully shutting down the script...")
    # Here you can perform cleanup actions if needed
    # For example, closing files or releasing resources
    exit(0)

# Set the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

def long_running_task():
    print("Starting a long-running task. Press Ctrl+C to interrupt.")
    try:
        while True:  # Simulating a long task
            print("Working...")
            time.sleep(1)  # Simulate doing work
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    long_running_task()