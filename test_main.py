import os
import pytest
from main import add_numbers, create_output_file

def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_create_output_file():
    """Test the create_output_file function."""
    file_path = create_output_file()
    
    # Check if file was created
    assert os.path.exists(file_path)
    
    # Check file contents
    with open(file_path, 'r') as f:
        content = f.read()
    
    assert "This file was created by the Python script" in content
    
    # Clean up the file after test
    os.remove(file_path)
