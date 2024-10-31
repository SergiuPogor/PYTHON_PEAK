import pytest

# Fixture for setting up test data
@pytest.fixture
def sample_data():
    return {
        'name': 'Alice',
        'age': 30,
        'location': 'Wonderland'
    }

# Test function using the fixture
def test_user_info(sample_data):
    assert sample_data['name'] == 'Alice'  # Check the name
    assert sample_data['age'] == 30        # Check the age
    assert sample_data['location'] == 'Wonderland'  # Check the location

# Additional test with parameterization
@pytest.mark.parametrize("input_name, expected", [
    ('Alice', 'Hello, Alice!'),
    ('Bob', 'Hello, Bob!'),
    ('Charlie', 'Hello, Charlie!')
])
def test_greeting(input_name, expected):
    assert greet(input_name) == expected

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    pytest.main()