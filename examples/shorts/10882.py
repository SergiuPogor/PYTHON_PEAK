import signal
import time

def signal_handler(sig, frame):
    print("Signal received! Cleaning up...")
    # Perform cleanup tasks here, like closing files or saving state
    exit(0)  # Exit the script

def main():
    # Register the signal handler for SIGINT
    signal.signal(signal.SIGINT, signal_handler)

    print("Long-running script started. Press Ctrl+C to interrupt...")
    try:
        while True:
            # Simulate a long-running task
            time.sleep(1)  # Replace with actual work
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()