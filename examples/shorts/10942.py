import weakref

class Resource:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is allocated.")

    def cleanup(self):
        print(f"{self.name} is cleaned up.")

# Create a resource object
resource = Resource("MyResource")

# Register a finalize callback to cleanup the resource
finalizer = weakref.finalize(resource, resource.cleanup)

# Check the status of the finalizer
print(f"Finalizer active: {finalizer.alive}")

# Delete the resource object
del resource

# Manually trigger garbage collection
import gc
gc.collect()

# At this point, you should see the cleanup message