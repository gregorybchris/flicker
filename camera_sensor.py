import os
import picamera
import uuid

from PIL import Image, ImageStat


class CameraSensor:
    def __init__(self, temp_dir='/tmp'):
        self._temp_dir = temp_dir
        self._camera = picamera.PiCamera()

    def probe(self, full_image=False):
        filename = f'photo-{uuid.uuid4()}.jpg'
        filepath = os.path.join(self._temp_dir, filename)
        self._camera.capture(filepath)
        image = Image.open(filepath)
        if full_image:
            return image
        brightness = self._get_brightness(image)
        return brightness

    def _get_brightness(self, image):
        grayscale = image.convert('L')
        stat = ImageStat.Stat(grayscale)
        return stat.mean[0]