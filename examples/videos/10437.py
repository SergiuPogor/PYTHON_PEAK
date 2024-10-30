import pytest

@pytest.fixture
def sample_data():
    # This fixture provides sample data for testing
    data = {
        'id': 1,
        'name': 'Test User',
        'age': 30
    }
    return data

@pytest.fixture(scope='module')
def database_connection():
    # Setup for a database connection
    connection = create_database_connection()
    yield connection  # This yields the connection for use in tests
    connection.close()  # Teardown after all tests in the module

def test_user_data(sample_data):
    assert sample_data['name'] == 'Test User'
    assert sample_data['age'] == 30

def test_database_query(database_connection):
    result = database_connection.query('SELECT * FROM users WHERE id = 1')
    assert result['name'] == 'Test User'

def create_database_connection():
    # Placeholder function for creating a database connection
    return MockDatabaseConnection()

class MockDatabaseConnection:
    # Mocking a database connection for demonstration
    def query(self, query):
        return {'id': 1, 'name': 'Test User'}

    def close(self):
        pass

if __name__ == "__main__":
    pytest.main()