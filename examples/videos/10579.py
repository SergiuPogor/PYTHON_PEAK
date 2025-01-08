import subprocess

def run_command(command):
    # Split the command into a list for subprocess
    command_list = command.split()

    try:
        # Execute the command securely
        result = subprocess.run(
            command_list, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Return the command output
        return result.stdout

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")
        return None

def main():
    # Example command to list files in the current directory
    command = "ls -la"
    
    # Run the command and print the output
    output = run_command(command)
    if output:
        print("Command output:")
        print(output)

if __name__ == "__main__":
    main()

# This code safely executes external commands using the subprocess module.
# It captures both standard output and error, ensuring the application runs securely.
# Always validate the command input before execution to prevent injection attacks.