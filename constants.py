import os

# Constant for the maximum number of clicks per second
MAX_CLICKS_PER_SECOND = 20

# Path constants for the configuration files
CONFIG_PATH = os.path.join(os.path.expanduser('~'), '.autoclicker', 'config.json')
LOG_PATH = os.path.join(os.path.expanduser('~'), '.autoclicker', 'app.log')

# Default values for settings
DEFAULT_SETTINGS = {
    'click_interval': 0.05,  # Interval between clicks in seconds
    'click_button': 'left',  # Button to click
    'repeat_count': 1000     # Number of times to click
}

# Error messages
ERROR_MESSAGES = {
    'file_not_found': 'Configuration file not found.',
    'invalid_setting': 'One or more settings are invalid.'
}

# Supported mouse buttons
MOUSE_BUTTONS = ['left', 'right', 'middle']

# Application version
APP_VERSION = '1.0.0'

# Debug mode
DEBUG_MODE = False

# Environment constants
ENVIRONMENT = os.getenv('AUTOMATION_ENV', 'development')
