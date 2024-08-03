class MyData:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

def compare_objects(obj1, obj2):
    if hash(obj1) == hash(obj2):
        print("Objects have the same hash value.")
    else:
        print("Objects have different hash values.")

# Create instances of MyData
data1 = MyData("example1")
data2 = MyData("example2")

# Compare the hash values of the objects
compare_objects(data1, data2)