import json

def load_config(file_path):
    """Load configuration from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            config_data = json.load(f)
            return config_data
    except FileNotFoundError:
        print(f"Error: {file_path} does not exist.")
        return {}
    except json.JSONDecodeError:
        print("Error: File is not a valid JSON.")
        return {}


def save_config(config_data, file_path):
    """Save configuration to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(config_data, f, indent=4)
            print(f"Configuration saved to {file_path}.")
    except IOError:
        print(f"Error: Could not write to {file_path}.")


# Example usage:
if __name__ == '__main__':
    config = load_config('settings.json')
    config['new_setting'] = 'value'
    save_config(config, 'settings.json')
