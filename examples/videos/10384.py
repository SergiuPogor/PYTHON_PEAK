import argparse

def main():
    parser = argparse.ArgumentParser(
        description='A custom command-line interface example.'
    )

    # Defining the main command
    parser.add_argument('command', type=str, choices=['add', 'remove', 'list'],
                        help='The command to execute: add, remove, or list items.')

    # Adding an optional argument for the 'add' command
    parser.add_argument('--name', type=str, help='Name of the item to add.')

    # Adding an optional argument for the 'remove' command
    parser.add_argument('--id', type=int, help='ID of the item to remove.')

    # Adding a flag for verbose output
    parser.add_argument('--verbose', action='store_true',
                        help='Enable verbose output.')

    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode enabled.")

    if args.command == 'add':
        if not args.name:
            print("Error: --name is required when adding an item.")
            return
        print(f"Adding item: {args.name}")

    elif args.command == 'remove':
        if args.id is None:
            print("Error: --id is required when removing an item.")
            return
        print(f"Removing item with ID: {args.id}")

    elif args.command == 'list':
        print("Listing all items...")

if __name__ == '__main__':
    main()