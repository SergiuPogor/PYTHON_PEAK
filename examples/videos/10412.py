# Import necessary libraries
import unittest
from unittest.mock import patch

# Example class to demonstrate mocking
class Database:
    def fetch_data(self):
        # Imagine this fetches data from a real database
        return "real data"

# Test case using unittest
class TestDatabase(unittest.TestCase):
    @patch.object(Database, 'fetch_data', return_value="mocked data")
    def test_fetch_data(self, mock_fetch):
        db = Database()
        # Call the method which we have mocked
        result = db.fetch_data()
        
        # Assert that the result is the mocked value
        self.assertEqual(result, "mocked data")
        mock_fetch.assert_called_once()  # Ensure fetch_data was called once

if __name__ == '__main__':
    unittest.main()