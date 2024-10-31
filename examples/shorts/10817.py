import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some integers.')

# Add arguments
parser.add_argument(
    'integers', 
    metavar='N', 
    type=int, 
    nargs='+',
    help='an integer for the accumulator'
)
parser.add_argument(
    '--sum', 
    dest='accumulate', 
    action='store_const', 
    const=sum, 
    default=max,
    help='sum the integers (default: find the max)'
)

# Parse the arguments
args = parser.parse_args()

# Print the result based on the selected action
result = args.accumulate(args.integers)
print(f'Result: {result}')

# To run this script from the command line:
# python script.py 1 2 3 4 --sum
# This would output: Result: 10

# To find the max instead, run:
# python script.py 1 2 3 4
# This would output: Result: 4