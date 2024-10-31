import argparse

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="A simple command-line application."
    )

    # Define command-line arguments
    parser.add_argument(
        '--name',
        type=str,
        required=True,
        help='Your name (required)'
    )
    parser.add_argument(
        '--age',
        type=int,
        default=18,
        help='Your age (default: 18)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Increase output verbosity'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Output the results
    if args.verbose:
        print(f"Verbose mode enabled.")
    print(f"Hello, {args.name}! You are {args.age} years old.")

if __name__ == "__main__":
    main()