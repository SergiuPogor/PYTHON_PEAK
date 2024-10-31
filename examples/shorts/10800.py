# Code Example: Using numpy Slicing and Memory Alignment for Faster Data Processing

import numpy as np
import time

# Generate a large random dataset for a realistic workload
data = np.random.rand(1000000)

# Accessing subarrays using slicing
def sum_slices(array):
    # Divide array into chunks and process separately
    slice_1, slice_2 = array[:500000], array[500000:]
    return np.sum(slice_1) + np.sum(slice_2)

# Compare numpy vs list processing times
data_list = data.tolist()  # Convert numpy array to list for comparison

# Benchmark numpy processing
start = time.time()
numpy_result = sum_slices(data)
numpy_time = time.time() - start

# Benchmark list processing for comparison
start = time.time()
list_result = sum(map(sum, [data_list[:500000], data_list[500000:]]))
list_time = time.time() - start

# Output results
print("Numpy processing time:", numpy_time)
print("List processing time:", list_time)
print("Numpy is faster by a factor of:", list_time / numpy_time)