# Using struct.pack for Binary Data Conversion

import struct

# Prepare data to be packed into binary format for storage/transmission
def pack_user_data(user_id, balance, is_active):
    # Pack an integer, float, and boolean into a binary format
    # > - big-endian, I - unsigned int, f - float, ? - boolean
    return struct.pack(">If?", user_id, balance, is_active)

# Example of packing user data
user_data = [
    {"user_id": 345, "balance": 105.75, "is_active": True},
    {"user_id": 678, "balance": 300.50, "is_active": False},
]

# Process and pack each user's data
packed_data = [pack_user_data(user["user_id"], user["balance"], user["is_active"]) for user in user_data]

# Display binary data for inspection or storage
for idx, data in enumerate(packed_data, 1):
    print(f"User {idx} Binary Data:", data)
    
# Unpack and read the binary data
def unpack_user_data(binary_data):
    return struct.unpack(">If?", binary_data)

# Example of unpacking binary data
unpacked_data = [unpack_user_data(data) for data in packed_data]
print("Unpacked Data:", unpacked_data)