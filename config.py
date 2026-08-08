import os

class Config:
    """Configuration settings for the application."""
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.debug = self.get_debug_mode()
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')

    def get_debug_mode(self):
        """Set debug mode based on environment."""
        if self.environment == 'production':
            return False
        return True

    def get_config(self):
        """Return the current configuration settings as a dictionary."""
        return {
            'environment': self.environment,
            'debug': self.debug,
            'database_url': self.database_url
        }

config = Config()