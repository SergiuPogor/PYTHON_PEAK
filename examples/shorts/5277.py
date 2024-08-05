# Example of using bytes() for binary data conversion
def convert_data_to_bytes(data):
    # Convert string data to bytes
    byte_data = bytes(data, 'utf-8')
    
    # Modify bytes data (e.g., write to file, send over network)
    # For demonstration, we'll just return the bytes
    return byte_data

def main():
    # Example string data to convert
    data = "Hello, Python!"
    
    # Convert to bytes and print result
    byte_data = convert_data_to_bytes(data)
    print(byte_data)

if __name__ == "__main__":
    main()
