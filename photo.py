import RPi.GPIO as GPIO
import time

import numpy as np


def probe_photoresistor(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.IN)

    count = 0
    while GPIO.input(pin) == GPIO.LOW:
        count += 1
    return count


def take_light_reading(pin, n_probes=20):
    measurements = [probe_photoresistor(pin) for _ in range(n_probes)]
    mean = np.mean(measurements)
    return mean


def run():
    pin = 18
    reading = take_light_reading(pin)
    print("Reading: ", reading)


if __name__ == '__main__':
    print("Running Photo")
    GPIO.setmode(GPIO.BOARD)
    try:
        run()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
