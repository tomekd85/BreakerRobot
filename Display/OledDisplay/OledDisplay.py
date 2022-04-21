import adafruit_ssd1306
import adafruit_displayio_ssd1306
import board
import digitalio
from PIL.Image import Image

from Display.Display import Display


class OledDisplay(Display):

    def __init__(self):
        self.WIDTH = 128
        self.HEIGHT = 64

    def show(self, image: Image):
        spi = board.SPI()
        oled_cs = digitalio.DigitalInOut(board.D5)
        oled_dc = digitalio.DigitalInOut(board.D6)
        oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)
