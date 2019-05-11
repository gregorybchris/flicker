import logging


def get_logger(filename='flicker_debug.log'):
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(filename)
    format_str = '%(asctime)s - %(levelname)-8s - %(message)s'
    formatter = logging.Formatter(format_str)  
    handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
