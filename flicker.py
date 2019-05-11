import argparse
import camera_sensor
import logging_utilities
import time

import numpy as np

from client import Client


PHOTO_SENSOR = 'photo'
CAMERA_SENSOR = 'camera'
ULTRASONIC_SENSOR = 'ultrasonic'

DEFAULT_READING_DECIMALS = 4


def send_message(api, message):
    response = api.post_message(message)
    print("Posted message: ", response.status_code, response.json())


def run(options, api):
    logger = logging_utilities.get_logger()
    sensor = camera_sensor.CameraSensor()
    logger.info("Camera sensor initialized")
    while True:
        reading = sensor.probe()
        reading = np.round(reading, DEFAULT_READING_DECIMALS)
        print(f"{reading}")
        logger.info(f"{reading}")
        if not options.dry:
            api.post_photo(reading)
        time.sleep(options.delay)


if __name__ == '__main__':
    print("Flicker is running")

    parser = argparse.ArgumentParser(description='Flicker monitoring')

    parser.add_argument('--message', '-m', help='Message to save')
    parser.add_argument('--type', '-t', default=CAMERA_SENSOR,
                        choices=[PHOTO_SENSOR, ULTRASONIC_SENSOR, CAMERA_SENSOR],
                        help='Type of monitoring to perform')
    parser.add_argument('--delay', '-d', type=int, default=30,
                        help='Delay between sensor probes')
    parser.add_argument('--dry', default=False, action='store_true',
                        help='Dry run with new API writes')
    
    args = parser.parse_args()

    api = Client()

    if args.message is not None:
        send_message(api, args.message)
        quit()

    elif args.type == CAMERA_SENSOR:
        run(args, api)
