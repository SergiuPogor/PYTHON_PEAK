import pytest

# Function to add two numbers
def add(a, b):
    return a + b

# Test function using pytest.mark.parametrize
@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 5, 15),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

# Run the tests
if __name__ == "__main__":
    pytest.main()