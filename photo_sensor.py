import time

import numpy as np
import RPi.GPIO as GPIO


class PhotoSensor:
    N_TRIALS = 20

    def __init__(self, pin=18):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self._pin = pin

    def probe(self):
        measurements = [self._trial() for _ in range(PhotoSensor.N_TRIALS)]

        # The first measurement will be different due to the
        # time it takes for the capacitor to charge
        measurements = measurements[1:]
        return np.mean(measurements)

    def _trial(self):
        GPIO.setup(self._pin, GPIO.OUT)
        GPIO.output(self._pin, GPIO.LOW)
        time.sleep(0.2)
        GPIO.setup(self._pin, GPIO.IN)

        count = 0
        while GPIO.input(self._pin) == GPIO.LOW:
            count += 1
        return count