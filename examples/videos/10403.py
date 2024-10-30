import pytest

# A sample function to demonstrate testing
def multiply(x, y):
    return x * y

# A fixture to provide common data for tests
@pytest.fixture
def sample_data():
    return [(2, 3, 6), (4, 5, 20), (0, 100, 0)]

# Test function using the fixture
def test_multiply(sample_data):
    for x, y, expected in sample_data:
        result = multiply(x, y)
        assert result == expected, f"Expected {expected}, but got {result}"

# A parameterized fixture for testing multiple cases
@pytest.fixture(params=[(1, 1, 1), (3, 3, 9), (5, 0, 0)])
def parameterized_data(request):
    return request.param

# Test function using the parameterized fixture
def test_parametrized_multiply(parameterized_data):
    x, y, expected = parameterized_data
    result = multiply(x, y)
    assert result == expected, f"Expected {expected}, but got {result}"

# If running this file directly, execute the tests
if __name__ == "__main__":
    pytest.main()