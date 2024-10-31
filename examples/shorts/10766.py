import sys

# Function to process multi-line input from sys.stdin
def process_input():
    print("Please enter your data (end with Ctrl+D):")
    
    # Read all lines from standard input
    data = sys.stdin.read()
    
    # Split the input data into lines
    lines = data.splitlines()
    
    # Process each line
    for line in lines:
        if line.strip():  # Ignore empty lines
            print("Processing:", line)

# Function call
if __name__ == "__main__":
    process_input()