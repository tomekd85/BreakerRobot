import time
from threading import Thread

import adafruit_ssd1306
import board
import digitalio
from PIL.Image import Image

from Display.Display import Display


class OledDisplay(Display):

    def __init__(self, refresh_rate: int = 3):
        self.WIDTH = 128
        self.HEIGHT = 64
        self.REFRESH_RATE = refresh_rate
        self.oled = self.__initialize_oled()
        self.display_update_thread = Thread(target=self.__reset_oled, daemon=True)
        self.display_update_thread.start()

    def __initialize_oled(self):
        spi = board.SPI()
        oled_reset = digitalio.DigitalInOut(board.D4)
        oled_cs = digitalio.DigitalInOut(board.D5)
        oled_dc = digitalio.DigitalInOut(board.D6)
        return adafruit_ssd1306.SSD1306_SPI(self.WIDTH, self.HEIGHT, spi, oled_dc, oled_reset, oled_cs)

    def fill(self, *args, **kwargs):
        self.oled.fill(*args, **kwargs)
        self.oled.show()

    def show(self, image: Image):
        self.oled.image(image)
        self.oled.show()

    def __reset_oled(self):
        while True:
            time.sleep(self.REFRESH_RATE)
            temp_buff = bytearray((self.oled.height // 8) * self.oled.width)
            temp_buff[:] = self.oled.buf
            self.oled.poweron()
            self.oled.init_display()
            self.oled.buf[:] = temp_buff
            self.oled.show()
