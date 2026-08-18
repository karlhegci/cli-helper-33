import logging
from typing import Optional

def setup_logger(name: str, log_file: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with the specified name and log file.
    
    Parameters:
        name (str): The name of the logger.
        log_file (Optional[str]): If specified, log to this file. Otherwise, log to stderr.
        level (int): Logging level (default is logging.INFO).
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Example of using the logger
if __name__ == "__main__":
    log = setup_logger('my_app', level=logging.DEBUG)
    log.debug('This is a debug message.')
    log.info('Informational message.')
    log.warning('Warning message.')
    log.error('Error message.')
    log.critical('Critical message.')
