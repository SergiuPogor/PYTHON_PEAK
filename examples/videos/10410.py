import pytest

# Function to add two numbers
def add(x, y):
    return x + y

# Test function using pytest
def test_add():
    # Test with positive numbers
    assert add(3, 5) == 8
    # Test with negative numbers
    assert add(-1, -1) == -2
    # Test with zero
    assert add(0, 5) == 5

# Using fixtures for setup
@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6

# Parameterized test to check multiple cases
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10),
])
def test_parametrized_add(a, b, expected):
    assert add(a, b) == expected

if __name__ == "__main__":
    pytest.main()