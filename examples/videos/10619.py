import subprocess

def run_command(command):
    try:
        # Run the command and capture output
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            check=True, 
            shell=True,
            timeout=10  # Timeout after 10 seconds
        )
        # Display the output and return code
        print("Command Output:", result.stdout)
        print("Return Code:", result.returncode)
    except subprocess.CalledProcessError as e:
        # Handle command errors
        print("An error occurred:", e.stderr)
        print("Return Code:", e.returncode)
    except subprocess.TimeoutExpired as e:
        # Handle command timeout
        print("Command timed out:", e.cmd)

# Example commands
commands = [
    "echo 'Hello, World!'",  # Simple command
    "ls -l",                  # List directory contents
    "cat /tmp/test/input.txt" # Read from a file (ensure the file exists)
]

# Run the example commands
for cmd in commands:
    run_command(cmd)