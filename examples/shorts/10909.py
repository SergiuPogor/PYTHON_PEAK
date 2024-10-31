import argparse

# Create main parser
parser = argparse.ArgumentParser(description="My CLI Tool with Subcommands")

# Set up subparsers
subparsers = parser.add_subparsers(
    title="Commands",
    description="Available Commands",
    dest="command"
)

# Example sub-command: `init`
parser_init = subparsers.add_parser(
    "init",
    help="Initialize the application setup."
)
parser_init.add_argument(
    "--force",
    action="store_true",
    help="Force re-initialization if already initialized."
)

# Example sub-command: `status`
parser_status = subparsers.add_parser(
    "status",
    help="Check the current application status."
)
parser_status.add_argument(
    "--verbose",
    action="store_true",
    help="Show detailed status information."
)

# Example sub-command: `deploy`
parser_deploy = subparsers.add_parser(
    "deploy",
    help="Deploy the application to production."
)
parser_deploy.add_argument(
    "--env",
    choices=["staging", "production"],
    default="staging",
    help="Specify the deployment environment."
)
parser_deploy.add_argument(
    "--dry-run",
    action="store_true",
    help="Run deployment as a test without actual changes."
)

# Parse and handle commands
args = parser.parse_args()

if args.command == "init":
    print("Initializing setup...")
    if args.force:
        print("Forced re-initialization.")
elif args.command == "status":
    print("Fetching application status...")
    if args.verbose:
        print("Detailed status information here.")
elif args.command == "deploy":
    print(f"Deploying to {args.env} environment...")
    if args.dry_run:
        print("Dry run mode: No changes will be made.")
else:
    parser.print_help()