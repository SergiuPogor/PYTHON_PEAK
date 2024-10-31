import pytest

# Function to add two numbers
def add(a, b):
    return a + b

# Test case for the add function
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Using fixtures for setup
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

# Test using the fixture
def test_sum(sample_data):
    assert sum(sample_data) == 15

# Running the tests
if __name__ == "__main__":
    pytest.main()