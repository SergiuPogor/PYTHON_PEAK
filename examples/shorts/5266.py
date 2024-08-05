def decode_message(encoded_message):
    # Decodes a message where each character is represented by its ASCII code
    decoded_message = ''.join(chr(int(code)) for code in encoded_message.split())
    return decoded_message

def encode_message(message):
    # Encodes a message by converting each character to its ASCII code
    encoded_message = ' '.join(str(ord(char)) for char in message)
    return encoded_message

# Example usage
encoded_message = '72 101 108 108 111 32 87 111 114 108 100'
decoded = decode_message(encoded_message)
print(f"Decoded Message: {decoded}")

message = 'Hello World'
encoded = encode_message(message)
print(f"Encoded Message: {encoded}")
