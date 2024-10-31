# Implementing a Singleton in Python using a metaclass

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # If instance doesn't exist, create it and store it in _instances
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# Example Singleton Class that represents a Database connection
class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, db_name):
        self.db_name = db_name
        print(f"Database '{self.db_name}' connected")

    def query(self, sql):
        return f"Executing '{sql}' on {self.db_name}"

# Testing the Singleton: Only one instance of DatabaseConnection should be created
def main():
    db1 = DatabaseConnection("MainDB")
    db2 = DatabaseConnection("MainDB")
    
    print(db1.query("SELECT * FROM users"))
    print(db2.query("SELECT * FROM products"))
    
    # Verifying singleton behavior by comparing instances
    print("Same instance:", db1 is db2)

main()