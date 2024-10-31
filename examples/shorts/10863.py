class MemoryEfficientClass:
    __slots__ = ('name', 'age')  # Define fixed attributes

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def main():
    # Creating multiple instances of the class
    people = [MemoryEfficientClass(f'Person {i}', i * 10) for i in range(1000)]
    
    # Display memory size of a single instance and all instances
    single_instance_size = MemoryEfficientClass('Example', 30).__sizeof__()
    total_size = sum(person.__sizeof__() for person in people)

    print(f'Single instance size: {single_instance_size} bytes')
    print(f'Total size for 1000 instances: {total_size} bytes')

if __name__ == "__main__":
    main()