import sys
import random
import string
from memory_profiler import memory_usage

# Generate a large dataset with many repeated strings
def generate_dataset(size):
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return [random.choice(words) for _ in range(size)]

# Without sys.intern(), high memory usage with repeated strings
dataset_no_intern = generate_dataset(1000000)

# Check memory usage without interning
def no_intern_memory_test():
    large_dataset = [word for word in dataset_no_intern]
    return large_dataset

print("Memory without interning:")
memory_no_intern = memory_usage(no_intern_memory_test, interval=0.1)
print(f"Memory used: {max(memory_no_intern) - min(memory_no_intern)} MB")

# With sys.intern(), memory is optimized by reusing the same string object
dataset_with_intern = [sys.intern(word) for word in dataset_no_intern]

# Check memory usage with interning
def intern_memory_test():
    interned_dataset = [sys.intern(word) for word in dataset_with_intern]
    return interned_dataset

print("\nMemory with interning:")
memory_with_intern = memory_usage(intern_memory_test, interval=0.1)
print(f"Memory used: {max(memory_with_intern) - min(memory_with_intern)} MB")

# Practical use case - a large dataset with user-input names having frequent repeats
def simulate_user_input():
    first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Wilson"]
    user_data = [(random.choice(first_names), random.choice(last_names)) for _ in range(100000)]
    
    interned_user_data = [(sys.intern(fname), sys.intern(lname)) for fname, lname in user_data]
    return interned_user_data

print("\nSimulating user input with repeated names:")
user_data_interned = simulate_user_input()
print("User data processed with interned names to save memory.")

# Observing memory optimization on user data
def user_data_memory():
    return [name for name in user_data_interned]

print("\nMemory on user data with interning:")
memory_user_data = memory_usage(user_data_memory, interval=0.1)
print(f"Memory used: {max(memory_user_data) - min(memory_user_data)} MB")