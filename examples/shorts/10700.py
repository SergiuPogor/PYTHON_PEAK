import pytest

# A function to add two numbers
def add(x, y):
    return x + y

# Parameterized test case using pytest
@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 5, 15),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

if __name__ == "__main__":
    pytest.main()