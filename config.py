import json
import os

DEFAULT_CONFIG = {
    'setting1': 'value1',
    'setting2': 'value2',
    'setting3': True
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def get(self, key):
        return self.config.get(key, None)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)
