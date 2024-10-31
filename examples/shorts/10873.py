import pytest
import tempfile
import os
from pathlib import Path

# Fixture to create a temporary directory for each test
@pytest.fixture
def temp_dir():
    # Create and yield a temporary directory, then clean up
    with tempfile.TemporaryDirectory() as dir_path:
        yield Path(dir_path)

# Fixture for mock database connection setup
@pytest.fixture
def mock_db():
    db_conn = {"status": "connected", "data": []}
    print("Mock database connected")
    yield db_conn
    db_conn["status"] = "disconnected"
    print("Mock database disconnected")

# Sample test that uses both fixtures
def test_create_file_in_temp_dir(temp_dir, mock_db):
    # Define a file path in the temporary directory
    file_path = temp_dir / "test_file.txt"
    
    # Write data to the file and store mock data in the db
    with open(file_path, "w") as f:
        f.write("Sample text content")
    mock_db["data"].append("Sample data entry")

    # Check if file exists and database has stored data correctly
    assert file_path.exists()
    assert mock_db["status"] == "connected"
    assert "Sample data entry" in mock_db["data"]

    # Read and verify file content
    with open(file_path, "r") as f:
        content = f.read()
    assert content == "Sample text content"