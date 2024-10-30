# This script demonstrates safe byte-to-string conversion using the decode() method.
# It includes error handling for various encoding issues.

def safe_byte_to_string(byte_data, encoding='utf-8'):
    """Convert bytes to a string using the specified encoding."""
    try:
        return byte_data.decode(encoding)
    except UnicodeDecodeError as e:
        print(f"Decoding error: {e}")
        # Handle the error by returning a placeholder or raising an error
        return None

def main():
    # Example byte data
    byte_valid = b'Hello, World!'
    byte_invalid = b'\x80\x81'

    # Valid conversion
    result_valid = safe_byte_to_string(byte_valid)
    print(f"Decoded string: {result_valid}")

    # Invalid conversion
    result_invalid = safe_byte_to_string(byte_invalid)
    if result_invalid is None:
        print("Failed to decode invalid byte data.")

if __name__ == "__main__":
    main()