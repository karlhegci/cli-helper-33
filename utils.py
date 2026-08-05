import os
import json

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    """Save JSON data to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def list_files(directory):
    """List all files in a directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def create_directory(directory):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def read_file(file_path):
    """Read the content of a file."""
    with open(file_path, 'r') as file:
        return file.read()


def write_file(data, file_path):
    """Write data to a file."""
    with open(file_path, 'w') as file:
        file.write(data)
