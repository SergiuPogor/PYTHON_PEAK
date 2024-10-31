import pytest

# A sample function to be tested
def add(a, b):
    return a + b

# A fixture that provides test data
@pytest.fixture
def input_data():
    return (2, 3)

# Parameterized test to check different inputs
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (10, 5, 15),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Test using the fixture
def test_add_with_fixture(input_data):
    a, b = input_data
    assert add(a, b) == 5