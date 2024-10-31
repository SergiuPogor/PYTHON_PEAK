import subprocess

# Example: Running a shell command to list files in a directory
command = ["ls", "-l", "/tmp/test"]

# Execute the command with subprocess.run, capture output and errors
try:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print("Command Output:\n", result.stdout)  # Print command output
except subprocess.CalledProcessError as e:
    print("Error executing command:", e.stderr)  # Print command error

# Advanced Example: Running multiple shell commands in a sequence
commands = [
    ["ls", "-l", "/tmp/test"],
    ["grep", "input", "/tmp/test/input.txt"],
    ["zip", "/tmp/test/archive.zip", "/tmp/test/input.txt"]
]

# Execute each command and capture outputs
for cmd in commands:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Output for '{' '.join(cmd)}':\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error with '{' '.join(cmd)}':", e.stderr)