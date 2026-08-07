import logging

# Configure the logger for the application
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def exception(self, message):
        self.logger.exception(message)

    def log_exception(self, e):
        if isinstance(e, Exception):
            self.logger.error(f'An error occurred: {str(e)}')
        else:
            self.logger.error('An unknown error occurred')

# Example usage:
# logger = Logger(__name__)
# try:
#     1 / 0  # This will raise an exception
# except Exception as e:
#     logger.log_exception(e)  
