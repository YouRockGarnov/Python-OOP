import pytest
import os
from solution import FileManager  # Замените "your_module" на фактическое имя вашего модуля

@pytest.fixture
def temp_file() -> str:
    filename = "temp_file.txt"
    with open(filename, "w") as tmp_file:
        return filename

def test_read_content(temp_file):
    with open(temp_file, 'w') as file:
        file.write("Hello, World!")

    with FileManager(temp_file) as file_manager:
        content = file_manager.read_content()
        assert content == "Hello, World!"

def test_write_content(temp_file):
    with FileManager(temp_file, 'w') as file_manager:
        file_manager.write_content("Testing write operation")

    with open(temp_file, 'r') as file:
        content = file.read()
        assert content == "Testing write operation"

def test_context_manager(temp_file):
    with FileManager(temp_file) as file_manager:
        assert file_manager.file.closed is False

    assert file_manager.file.closed is True

def test_file_not_found_exception(temp_file):
    with pytest.raises(FileNotFoundError):
        with FileManager("nonexistent_file.txt") as file_manager:
            pass

def test_permission_error_exception(temp_file):
    with pytest.raises(PermissionError):
        with FileManager("/etc/some_protected_file.txt", 'w') as file_manager:
            pass
