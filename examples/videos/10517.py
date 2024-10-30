import pytest

# Sample function to be tested
def calculate_discount(price, discount):
    if price < 0 or discount < 0:
        raise ValueError("Price and discount must be non-negative")
    return price * (1 - discount / 100)

# Fixture for setup
@pytest.fixture
def sample_data():
    return [
        (100, 10, 90),
        (200, 25, 150),
        (50, 50, 25)
    ]

# Parameterized test function
@pytest.mark.parametrize("price, discount, expected", [
    (100, 10, 90),
    (200, 25, 150),
    (50, 50, 25)
])
def test_calculate_discount(price, discount, expected):
    result = calculate_discount(price, discount)
    assert result == expected

# Test for exceptions
def test_calculate_discount_negative_values():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)
    with pytest.raises(ValueError):
        calculate_discount(100, -10)

# Main execution to run tests
if __name__ == "__main__":
    pytest.main()