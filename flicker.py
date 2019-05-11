import argparse
import camera_sensor
import photo_sensor
import time
import ultrasonic_sensor

import numpy as np

from client import Client
from gpio_utilities import gpio_safe


def send_message(api, message):
    response = api.post_message(message)
    print("Posted message: ", response.status_code, response.json())


@gpio_safe
def run_photo(api):
    pin = 18

    sensor = photo_sensor.PhotoSensor()
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

    sensor = ultrasonic_sensor.UltrasonicSensor()
    sensor.setup(trigger_pin=trigger_pin, echo_pin=echo_pin)
    print("Ultrasonic sensor initialized")

    while True:
        reading = sensor.probe()
        reading = np.round(reading, 4)
        print(f"{reading}cm")
        api.post_ultrasonic(reading)
        time.sleep(delay)


def run_camera(api):
    delay = 5

    sensor = camera_sensor.CameraSensor()
    sensor.setup()
    print("Camera sensor initialized")

    while True:
        reading = sensor.probe()
        print(f"{reading}")
        # api.post_camera(reading)
        time.sleep(delay)


if __name__ == '__main__':
    print("Flicker is running")

    parser = argparse.ArgumentParser(description='Flicker monitoring')

    parser.add_argument('--message', '-m', help='Message to save')
    parser.add_argument('--type', '-t', default='camera',
                        choices=['photo', 'ultrasonic', 'camera'],
                        help='Type of monitoring to perform')

    args = parser.parse_args()

    api = Client()

    if args.message is not None:
        send_message(api, args.message)
        quit()

    if args.type == 'photo':
        run_photo(api)
    elif args.type == 'ultrasonic':
        run_ultrasonic(api)
    elif args.type == 'camera':
        run_camera(api)