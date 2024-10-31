import subprocess

def run_command(command):
    try:
        # Execute the command and capture output
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        # Decode the byte output to string
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        # Handle errors during command execution
        return f"Error: {e.output.decode('utf-8')}"

# Example usage
if __name__ == "__main__":
    # Run a simple command
    command = ['echo', 'Hello, World!']
    result = run_command(command)
    print(result)

    # Running a command that may fail
    command_fail = ['ls', '/non_existent_directory']
    result_fail = run_command(command_fail)
    print(result_fail)