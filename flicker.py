import pprint
import time

from client import Client
from gpio_utilities import gpio_safe
from ultrasonic import UltrasonicSensor


def make_messages(api):
    message = "Flicker!"
    print("Posting message: ", message)
    response = api.post_message(message)
    print("Received: ", response.status_code, response.json())

    response = api.get_messages()
    messages = response.json()['messages']
    print("Get messages:")
    pprint.pprint(messages)


@gpio_safe
def run_ultrasonic(api):
    trigger_pin = 17
    echo_pin = 18

    sensor = UltrasonicSensor()
    sensor.setup(trigger_pin=trigger_pin, echo_pin=echo_pin)
    print("Ultrasonic sensor initialized")
    while True:
        reading = sensor.probe()
        print(f"{reading}cm")
        time.sleep(3)
        api.post_ultrasonic(reading)


if __name__ == '__main__':
    print("Flicker is running")

    api = Client()
    run_ultrasonic(api)
