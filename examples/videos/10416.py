import pytest

@pytest.fixture
def setup_database():
    # Setup a mock database connection
    db = DatabaseConnection()
    db.connect()
    yield db  # This will return the database connection to the test
    db.disconnect()  # Cleanup after test

def test_insert_data(setup_database):
    db = setup_database
    # Use the db connection to insert data
    result = db.insert({"name": "Alice", "age": 30})
    
    assert result == True  # Verify insertion was successful

def test_query_data(setup_database):
    db = setup_database
    # Insert data before querying
    db.insert({"name": "Bob", "age": 25})
    
    # Now query for the data
    result = db.query("SELECT * FROM users WHERE name='Bob'")
    
    assert result == [{"name": "Bob", "age": 25}]  # Check returned data

def test_update_data(setup_database):
    db = setup_database
    # Insert initial data
    db.insert({"name": "Charlie", "age": 35})
    
    # Update the data
    db.update("UPDATE users SET age = 36 WHERE name='Charlie'")
    result = db.query("SELECT * FROM users WHERE name='Charlie'")
    
    assert result == [{"name": "Charlie", "age": 36}]  # Verify update