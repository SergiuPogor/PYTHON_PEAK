import subprocess

# Basic command to list files in a directory and capture output
result = subprocess.run(["ls", "-la", "/tmp/test"], capture_output=True, text=True)

# Print output if successful, else print error
if result.returncode == 0:
    print("Command output:\n", result.stdout)
else:
    print("Command failed with error:\n", result.stderr)

# Execute a more complex command: search file content, using 'grep' and capturing error if file not found
try:
    search_result = subprocess.run(["grep", "Sample text", "/tmp/test/input.txt"],
                                   capture_output=True, text=True, check=True)
    print("Search output:\n", search_result.stdout)
except subprocess.CalledProcessError as e:
    print("Error during search:", e.stderr)

# Demonstrating piping: count lines in a file after filtering, simulating "grep | wc -l"
grep_process = subprocess.Popen(["grep", "-i", "Sample", "/tmp/test/input.txt"], stdout=subprocess.PIPE)
wc_process = subprocess.run(["wc", "-l"], stdin=grep_process.stdout, capture_output=True, text=True)

# Ensure all outputs are processed
grep_process.stdout.close()
wc_process.check_returncode()

# Display count result
print("Line count for filtered content:", wc_process.stdout.strip())