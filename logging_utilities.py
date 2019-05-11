import logging

def get_logger(filename='flicker_debug.log'):
    logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler(filename)
    # f_handler.setLevel(logging.ERROR)
    logger.addHandler(f_handler)
    return logger