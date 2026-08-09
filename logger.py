import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file, max_bytes=5*1024*1024, backup_count=3):
    """
    Set up a rotating logger.

    Args:
        log_file (str): The path to the log file.
        max_bytes (int): Maximum size of the log file before rotation.
        backup_count (int): Maximum number of backup files to keep.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

logger = setup_logger('app.log')