import os
import json
from typing import Any, Dict, List

def load_json(file_path: str) -> Dict[str, Any]:
    """Load a JSON file and return its content as a dictionary."""
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path: str, data: Dict[str, Any]) -> None:
    """Save a dictionary as a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def list_files(directory: str) -> List[str]:
    """Return a list of files in the given directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def is_json_file(file_path: str) -> bool:
    """Check if a file is a valid JSON file based on its extension."""
    return file_path.endswith('.json')


def read_file(file_path: str) -> str:
    """Read the content of a text file and return it as a string."""
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path: str, content: str) -> None:
    """Write a string to a text file."""
    with open(file_path, 'w') as file:
        file.write(content)