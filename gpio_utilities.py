import RPi.GPIO as GPIO


def gpio_safe(func):
    """
    Decorator for GPIO KeyboardInterrupts.

    Decorate a function with this to safely cleanup
    when a program using GPIO is terminated.
    """
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            GPIO.cleanup()
    return wrapper
