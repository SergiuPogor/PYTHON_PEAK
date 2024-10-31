# Comparing performance of membership tests with set and list
import time

# Sample data
data_list = list(range(1000000))  # List of numbers from 0 to 999999
data_set = set(data_list)  # Set created from the list

# Function to test membership in list
def test_list_membership(value):
    return value in data_list

# Function to test membership in set
def test_set_membership(value):
    return value in data_set

# Test value
test_value = 999999

# Measure time for list membership test
start_time = time.time()
result_list = test_list_membership(test_value)
list_time = time.time() - start_time

# Measure time for set membership test
start_time = time.time()
result_set = test_set_membership(test_value)
set_time = time.time() - start_time

# Show results
print(f"List membership result: {result_list} (Time taken: {list_time:.6f} seconds)")
print(f"Set membership result: {result_set} (Time taken: {set_time:.6f} seconds)")

# Demonstrates the speed advantage of using sets over lists