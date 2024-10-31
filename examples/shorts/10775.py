import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="Process some integers.")

# Define arguments
parser.add_argument(
    '-n', '--numbers', type=int, nargs='+', required=True,
    help='A list of integers to process'
)
parser.add_argument(
    '-o', '--operation', choices=['sum', 'avg'], default='sum',
    help='Operation to perform on the numbers'
)

# Parse arguments
args = parser.parse_args()

# Perform the specified operation
if args.operation == 'sum':
    result = sum(args.numbers)
else:
    result = sum(args.numbers) / len(args.numbers)

# Print the result
print(f"The result of the {args.operation} is: {result}")