import sqlite3

def setup_in_memory_db():
    # Create an in-memory SQLite database
    connection = sqlite3.connect(":memory:")  # Using ':memory:' for in-memory DB
    cursor = connection.cursor()

    # Create a table
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    # Insert sample data
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
    
    # Commit changes
    connection.commit()

    return connection

def fetch_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

if __name__ == "__main__":
    db_connection = setup_in_memory_db()
    users = fetch_users(db_connection)
    print("Users in the database:", users)  # Output: Users in the database: [(1, 'Alice', 30), (2, 'Bob', 25)]