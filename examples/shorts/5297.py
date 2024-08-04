class Base:
    def greet(self):
        print("Hello from Base")

class A(Base):
    def greet(self):
        super().greet()  # Calls greet() from Base
        print("Hello from A")

class B(Base):
    def greet(self):
        super().greet()  # Calls greet() from Base
        print("Hello from B")

class C(A, B):
    def greet(self):
        super().greet()  # Calls greet() from A and B in method resolution order
        print("Hello from C")

# Usage example
obj = C()
obj.greet()

# Output:
# Hello from Base
# Hello from B
# Hello from A
# Hello from C