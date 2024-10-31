import subprocess

# 1. Run a simple shell command and capture output
result = subprocess.run(
    ["echo", "Hello, World!"], 
    capture_output=True, 
    text=True
)
print("Output:", result.stdout)  # Expected Output: Hello, World!

# 2. Run a shell command with error handling (Example: listing files)
try:
    result = subprocess.run(
        ["ls", "-l", "/non_existent_directory"],
        capture_output=True,
        text=True,
        check=True  # This raises an exception on non-zero exit codes
    )
except subprocess.CalledProcessError as e:
    print("Error Code:", e.returncode)  # Capturing error code
    print("Error Output:", e.stderr)    # Capturing error message

# 3. Using input for a shell command (Example: using grep with piped input)
result = subprocess.run(
    ["grep", "Python"],
    input="Python is amazing!\nLearning Python subprocess.",
    capture_output=True,
    text=True
)
print("Filtered Output:", result.stdout)  # Expected Output: "Python is amazing!"

# 4. Running an external program with multiple arguments
# Example: Check disk space using `df` command
result = subprocess.run(
    ["df", "-h", "--output=source,size,used,avail"],
    capture_output=True,
    text=True
)
print("Disk Usage Info:\n", result.stdout)  # Displays disk usage details

# 5. Use subprocess.run() to zip files (simulating shell script in Python)
# Note: Replace paths if they differ
result = subprocess.run(
    ["zip", "-r", "/tmp/test/backup.zip", "/tmp/test/input.txt"],
    capture_output=True,
    text=True
)
print("Zip Output:", result.stdout)  # Expected Output: Info about the zipped files