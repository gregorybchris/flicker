import RPi.GPIO as GPIO
import time

import numpy as np


def probe(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.setup(pin, GPIO.IN)

    count = 0
    while GPIO.input(pin) == GPIO.LOW:
        count += 1
    return count


def take_light_reading(pin, n_probes=10):
    measurements = np.array([probe(pin) for _ in range(n_probes)])

    # The first probe will be different due to the capacitor charging
    measurements = measurements[1:]

    mean = np.mean(measurements)
    std = np.std(measurements)
    print("mean: ", mean)
    print("std: ", std)
    return mean


def gpio_safe(func):
    def wrapper():
        try:
            func()
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()
            print("Cleaned up GPIO")
    return wrapper


@gpio_safe
def run():
    pin = 18
    while True:
        reading = take_light_reading(pin, n_probes=20)
        # print(reading)


if __name__ == '__main__':
    print("Reading photoresistor...")
    GPIO.setmode(GPIO.BOARD)
    run()
