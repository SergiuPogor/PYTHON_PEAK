import subprocess

# Define the shell command to execute
command = ["ls", "-l", "/tmp/test"]

# Running the shell command and capturing output
try:
    result = subprocess.run(
        command,
        capture_output=True,   # Capture stdout and stderr
        text=True,             # Return as a string instead of bytes
        timeout=5,             # Limit execution time in seconds
        check=True             # Raises CalledProcessError on non-zero exit
    )
    # Output result and errors if any
    print("Command Output:\n", result.stdout)
    print("Command Error (if any):\n", result.stderr)

except subprocess.CalledProcessError as e:
    # Command failed, handle the error
    print("Error occurred:", e)
    print("Error Output:\n", e.stderr)

except subprocess.TimeoutExpired as e:
    # Command took too long, timeout exceeded
    print("Command timed out:", e)