import contextlib
import os

@contextlib.contextmanager
def temporary_file(file_path):
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Create the temporary file
    file = open(file_path, 'w')
    try:
        yield file
    finally:
        # Ensure file is closed and deleted
        file.close()
        os.remove(file_path)

# Example usage
with temporary_file('/tmp/test/sample.txt') as f:
    f.write("Hello, this file is temporary!")
    f.flush()  # Ensures data is written to disk

# Real use-case: Context manager for database connection
import sqlite3

@contextlib.contextmanager
def database_connection(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        # Commit and close the database connection
        conn.commit()
        conn.close()

# Example usage of database connection
db_path = '/tmp/test/example.db'
with database_connection(db_path) as cursor:
    # Creating a table
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    # Inserting data
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    # Query data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Nested context managers: Using multiple resources
with temporary_file('/tmp/test/output.txt') as temp_file, \
     database_connection('/tmp/test/example.db') as db_cursor:
    temp_file.write("Logging user data to temporary file...\n")
    db_cursor.execute("SELECT * FROM users")
    for user in db_cursor.fetchall():
        temp_file.write(f"User: {user}\n")