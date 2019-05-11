import logging


def get_logger(filename='flicker_debug.log'):
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(filename)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
