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