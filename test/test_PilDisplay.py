from time import sleep
from unittest import TestCase

from PIL import Image

from Display.PilDisplay.PilDisplay import PilDisplay


class TestPilDisplay(TestCase):

    WIDTH = 128
    HEIGHT = 64

    def test_show(self):
        image = Image.new("1", (self.WIDTH, self.HEIGHT))
        display = PilDisplay()
        display.show(image)
        sleep(5)
