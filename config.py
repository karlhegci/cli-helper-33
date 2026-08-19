import os
import json

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, config_file='config.json'):  
        self.config_file = config_file
        self.settings = {}
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise ConfigError(f'Config file {self.config_file} does not exist.')
        try:
            with open(self.config_file, 'r') as f:
                self.settings = json.load(f)
        except json.JSONDecodeError:
            raise ConfigError('Error decoding JSON from config file.')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {e}')

    def get_setting(self, key):
        if key not in self.settings:
            raise ConfigError(f'Setting {key} not found in config.')
        return self.settings[key]

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            raise ConfigError(f'Failed to save config: {e}')