import argparse

def process_data(file_path, delimiter, header):
    """Process the given file."""
    print(f"Processing file: {file_path}")
    print(f"Using delimiter: '{delimiter}'")
    print(f"Header present: {header}")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Process some data files.')
    
    # Adding arguments
    parser.add_argument('file', type=str, 
                        help='Path to the data file to process')
    parser.add_argument('--delimiter', type=str, default=',',
                        help='Delimiter used in the file (default: ",")')
    parser.add_argument('--header', action='store_true',
                        help='Indicate if the file has a header row')

    # Parse the arguments
    args = parser.parse_args()

    # Call the process_data function
    process_data(args.file, args.delimiter, args.header)

if __name__ == "__main__":
    main()