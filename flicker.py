import argparse
import camera_sensor
import logging_utilities
import time

import numpy as np

from client import Client


def send_message(options, api):
    response = api.post_message(options.message)
    print("Posted message: ", response.status_code, response.json())


def run(options, api):
    logger = logging_utilities.get_logger()
    sensor = camera_sensor.CameraSensor()
    logger.info("Camera sensor initialized")
    while True:
        reading = sensor.probe()
        reading = np.round(reading, 4)
        print(f"{reading}")
        logger.info(f"Camera reading: {reading}")
        if not options.dry:
            api.post_photo(reading)
        time.sleep(options.delay)


if __name__ == '__main__':
    print("Flicker is running")

    parser = argparse.ArgumentParser(description='Flicker monitoring')
    parser.add_argument('--message', '-m', help='Message to save')
    parser.add_argument('--delay', '-d', type=int, default=30,
                        help='Delay between sensor probes')
    parser.add_argument('--dry', default=False, action='store_true',
                        help='Dry run with new API writes')
    args = parser.parse_args()

    api = Client()

    if args.message is not None:
        send_message(api, args.message)
        quit()

    run(args, api)
