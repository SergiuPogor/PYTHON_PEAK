def convert_bytes_to_string(byte_data, encoding='utf-8'):
    """
    Safely convert bytes to a string using the specified encoding.
    Handle decoding errors gracefully.
    """
    try:
        # Decode the byte data using the specified encoding
        return byte_data.decode(encoding)
    except UnicodeDecodeError as e:
        # Handle decoding errors
        print(f"Decoding error: {e}")
        return None

# Example usage with various byte data
byte_examples = [
    b'Hello, World!',        # Valid UTF-8
    b'\xff\xfeH\x00e\x00l\x00l\x00o\x00',  # UTF-16
    b'\x80\x81\x82',        # Invalid UTF-8 sequence
]

for byte_data in byte_examples:
    result = convert_bytes_to_string(byte_data)
    if result is not None:
        print(f"Converted string: {result}")
    else:
        print("Failed to convert bytes to string.")