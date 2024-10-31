import argparse

# Function to create a flexible command-line interface
def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    
    # Adding required argument
    parser.add_argument("integers", type=int, nargs="+", help="an integer for the accumulator")
    
    # Adding optional argument with default value
    parser.add_argument("--sum", dest="accumulate", action="store_const",
                        const=sum, default=max, help="sum the integers (default: find the max)")
    
    # Parsing arguments
    args = parser.parse_args()
    
    # Performing the operation based on the provided arguments
    result = args.accumulate(args.integers)
    
    print("Result:", result)

# Entry point
if __name__ == "__main__":
    main()