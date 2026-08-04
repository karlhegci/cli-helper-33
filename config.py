import json
import os

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'log_level': 'info'
}

class ConfigLoader:
    def __init__(self, config_path=None):
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()  # Start with default values

    def load(self):
        if self.config_path and os.path.isfile(self.config_path):
            with open(self.config_path, 'r') as file:
                try:
                    user_config = json.load(file)
                    self.config.update(user_config)  # Update defaults with user config
                except json.JSONDecodeError:
                    print('Error: Invalid JSON in configuration file.')
                    return
        return self.config

# Example of using ConfigLoader
if __name__ == '__main__':
    loader = ConfigLoader('config.json')  # Path to user config
    config = loader.load()
    print(config)  # Display the final configuration after loading
