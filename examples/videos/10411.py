# Function to demonstrate string formatting using both methods
def demonstrate_string_formatting(name, age, job):
    # Using f-strings (Python 3.6+)
    f_string_output = f"My name is {name}, I am {age} years old, and I work as a {job}."
    
    # Using str.format()
    format_string_output = "My name is {}, I am {} years old, and I work as a {}.".format(name, age, job)

    return f_string_output, format_string_output

# Benchmarking the performance of both methods
import time

def benchmark_string_formatting():
    name = "Alice"
    age = 30
    job = "developer"

    # Timing f-string
    start_time = time.time()
    for _ in range(100000):
        demonstrate_string_formatting(name, age, job)
    f_string_time = time.time() - start_time

    # Timing str.format()
    start_time = time.time()
    for _ in range(100000):
        demonstrate_string_formatting(name, age, job)
    format_string_time = time.time() - start_time

    return f_string_time, format_string_time

# Running the benchmark
if __name__ == "__main__":
    f_time, fmt_time = benchmark_string_formatting()
    print(f"F-string time: {f_time:.4f}s")
    print(f"str.format() time: {fmt_time:.4f}s")