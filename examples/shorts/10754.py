# Python argparse for building complex CLI with subcommands and default values

import argparse

# Set up main parser
parser = argparse.ArgumentParser(description="File Operations Tool")
subparsers = parser.add_subparsers(dest="command")

# Subcommand: view file content
view_parser = subparsers.add_parser("view", help="Display file content")
view_parser.add_argument("file", type=str, help="Path to the file")

# Subcommand: create a new file with default content if no input is given
create_parser = subparsers.add_parser("create", help="Create a new file")
create_parser.add_argument("file", type=str, help="Path to the new file")
create_parser.add_argument("--content", type=str, default="Default file content",
                           help="Content to write in the file (optional)")

# Subcommand: list directory contents with optional depth
list_parser = subparsers.add_parser("list", help="List directory contents")
list_parser.add_argument("directory", type=str, help="Directory path")
list_parser.add_argument("--depth", type=int, default=1,
                         help="Depth level for listing (default is 1)")

# Parse and handle commands
args = parser.parse_args()

if args.command == "view":
    with open(args.file, 'r') as f:
        print("File Content:\n", f.read())

elif args.command == "create":
    with open(args.file, 'w') as f:
        f.write(args.content)
    print(f"File '{args.file}' created with content:\n", args.content)

elif args.command == "list":
    import os

    def list_dir(path, depth):
        if depth < 1:
            return
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            if level < depth:
                print("Directory:", root)
                for f in files:
                    print("  -", f)

    list_dir(args.directory, args.depth)