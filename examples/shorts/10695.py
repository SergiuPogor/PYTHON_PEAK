import argparse

# Create a parser object
parser = argparse.ArgumentParser(description="Process some integers.")

# Adding command line arguments
parser.add_argument("integers", metavar="N", type=int, nargs="+",
                    help="an integer for the accumulator")
parser.add_argument("--sum", dest="accumulate", action="store_const",
                    const=sum, default=max,
                    help="sum the integers (default: find the max)")

# Parse the arguments
args = parser.parse_args()

# Calculate the result based on user input
result = args.accumulate(args.integers)

# Output the result
print(result)  # Output the sum or max of the integers