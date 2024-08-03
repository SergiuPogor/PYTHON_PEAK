class Animal:
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

def check_class(cls):
    if issubclass(cls, Mammal):
        print(f"{cls.__name__} is a subclass of Mammal.")
    else:
        print(f"{cls.__name__} is not a subclass of Mammal.")

# Example usage
check_class(Dog)    # Output: Dog is a subclass of Mammal.
check_class(Bird)   # Output: Bird is not a subclass of Mammal.