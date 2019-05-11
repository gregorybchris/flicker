import time

import RPi.GPIO as GPIO


class UltrasonicSensor:
    def __init__(self, trigger_pin=17, echo_pin=18):
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
