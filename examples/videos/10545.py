# Demonstrating the memory-saving capabilities of __slots__ in a Python class

import sys

# A traditional class without __slots__:
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

# Class with __slots__ defined to save memory by avoiding instance dictionaries
class EmployeeOptimized:
    __slots__ = ['name', 'position', 'salary']
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

# Creating multiple instances of both classes and comparing memory usage
def calculate_memory_usage():
    employees_standard = [Employee(f"Name{i}", "Engineer", 70000 + i * 1000) for i in range(10000)]
    employees_optimized = [EmployeeOptimized(f"Name{i}", "Engineer", 70000 + i * 1000) for i in range(10000)]
    
    standard_memory = sys.getsizeof(employees_standard)
    optimized_memory = sys.getsizeof(employees_optimized)

    print("Memory used by traditional class:", standard_memory, "bytes")
    print("Memory used by class with __slots__:", optimized_memory, "bytes")

calculate_memory_usage()

# Additional Example: Extending a class with __slots__
class EmployeeExtended(EmployeeOptimized):
    __slots__ = ['bonus']
    
    def __init__(self, name, position, salary, bonus):
        super().__init__(name, position, salary)
        self.bonus = bonus

# Calculating memory with extended class
def calculate_extended_memory_usage():
    employees_extended = [EmployeeExtended(f"Name{i}", "Manager", 90000 + i * 2000, 5000) for i in range(10000)]
    extended_memory = sys.getsizeof(employees_extended)
    
    print("Memory used by extended class with __slots__:", extended_memory, "bytes")

calculate_extended_memory_usage()