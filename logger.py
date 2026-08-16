import logging
from logging.handlers import RotatingFileHandler

# Configure the logger
logger = logging.getLogger('cli_helper')
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
handler = RotatingFileHandler('cli_helper.log', maxBytes=5*1024*1024, backupCount=3)
handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example log messages
logger.debug('Debugging information')
logger.info('Informational message')
logger.warning('A warning occurred')
logger.error('An error has happened')
logger.critical('Critical issue')
