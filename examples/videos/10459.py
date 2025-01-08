import struct

def create_binary_file(filename, data):
    # Create a binary file and write packed data to it
    with open(filename, 'wb') as file:
        for item in data:
            # Packing an integer and a float into binary format
            packed_data = struct.pack('if', item['id'], item['value'])
            file.write(packed_data)

def read_binary_file(filename):
    # Read the binary file and unpack data
    with open(filename, 'rb') as file:
        while True:
            # Reading 8 bytes: 4 bytes for int, 4 bytes for float
            bytes_read = file.read(8)
            if not bytes_read:
                break
            # Unpacking the data
            id_value, float_value = struct.unpack('if', bytes_read)
            print(f"ID: {id_value}, Value: {float_value}")

def main():
    filename = '/tmp/test/data.bin'
    # Example data to pack
    data = [{'id': 1, 'value': 10.5}, {'id': 2, 'value': 20.75}, {'id': 3, 'value': 30.0}]
    create_binary_file(filename, data)  # Create binary file with data
    read_binary_file(filename)  # Read and display data from binary file

if __name__ == "__main__":
    main()  # Run the main function