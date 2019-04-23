import time

import numpy as np

from client import Client
from gpio_utilities import gpio_safe
from sensors import PhotoSensor, UltrasonicSensor


def send_message(api, message):
    response = api.post_message(message)
    print("Posted message: ", response.status_code, response.json())


@gpio_safe
def run_photo(api):
    pin = 18

    sensor = PhotoSensor()
    sensor.setup(pin=pin)
    print("Photo sensor initialized")

    while True:
        reading = sensor.probe()
        reading = np.round(reading, 4)
        print(f"{reading}")
        time.sleep(0.5)
        api.post_photo(reading)


@gpio_safe
def run_ultrasonic(api):
    trigger_pin = 17
    echo_pin = 18
    delay = 5

    sensor = UltrasonicSensor()
    sensor.setup(trigger_pin=trigger_pin, echo_pin=echo_pin)
    print("Ultrasonic sensor initialized")

    while True:
        reading = sensor.probe()
        reading = np.round(reading, 4)
        print(f"{reading}cm")
        time.sleep(delay)
        api.post_ultrasonic(reading)


if __name__ == '__main__':
    print("Flicker is running")

    api = Client()
    run_ultrasonic(api)
