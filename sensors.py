import time

import numpy as np
import RPi.GPIO as GPIO

from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self):
        self.setup()

    @abstractmethod
    def setup(self, **pin_config):
        """
        Assign GPIO pins for the sensor.

        :param pin_config: Kwargs for pin ON vs OFF.
        """
        ...

    @abstractmethod
    def probe(self, *args, **kwargs):
        """
        Probe the sensor to get a value.
        """
        ...


class PhotoSensor(Sensor):
    N_TRIALS = 20

    def setup(self, pin=18):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self._pin = pin

    def probe(self):
        measurements = [self._trial() for _ in range(PhotoSensor.N_TRIALS)]

        # The first probe will be different due to the capacitor charging
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


class UltrasonicSensor(Sensor):
    def setup(self, trigger_pin=17, echo_pin=18):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
        self._trigger = trigger_pin
        self._echo = echo_pin

    def probe(self):
        GPIO.output(self._trigger, 0)
        time.sleep(0.000002)
        GPIO.output(self._trigger, 1)
        time.sleep(0.00001)
        GPIO.output(self._trigger, 0)

        while GPIO.input(self._echo) == 0:
            off_time = time.time()
        while GPIO.input(self._echo) == 1:
            total_time = time.time() - off_time
        return self._calibrate_echo(total_time)

    def _calibrate_echo(self, echo):
        # TODO: Allow custom echo calibration
        return echo * 340 / 2 * 100
