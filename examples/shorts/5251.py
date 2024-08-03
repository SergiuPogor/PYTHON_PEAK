class ExampleClass:
    def __init__(self):
        self.existing_attr = "I'm here!"

def check_attributes(obj):
    # Check if 'existing_attr' exists in obj
    if hasattr(obj, 'existing_attr'):
        print("Attribute 'existing_attr' is present.")
    else:
        print("Attribute 'existing_attr' is missing.")

    # Check if 'missing_attr' exists in obj
    if hasattr(obj, 'missing_attr'):
        print("Attribute 'missing_attr' is present.")
    else:
        print("Attribute 'missing_attr' is missing.")

# Create an instance of ExampleClass
example = ExampleClass()

# Call the function to check attributes
check_attributes(example)