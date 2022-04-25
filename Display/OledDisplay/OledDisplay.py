import time
from threading import Thread

import adafruit_ssd1306
import board
import digitalio
from PIL import ImageFont, ImageDraw, Image

from Display.Display import Display


class OledDisplay(Display):

    def __init__(self, refresh_rate: float = 3):
        self.WIDTH = 128
        self.HEIGHT = 64
        self.REFRESH_RATE = refresh_rate
        self.oled = self.__initialize_oled()
        # self.display_update_thread = Thread(target=self.__reset_oled, daemon=True)
        # self.display_update_thread.start()

    def __initialize_oled(self):
        spi = board.SPI()
        oled_reset = digitalio.DigitalInOut(board.D4)
        oled_cs = digitalio.DigitalInOut(board.D5)
        oled_dc = digitalio.DigitalInOut(board.D6)
        return adafruit_ssd1306.SSD1306_SPI(self.WIDTH, self.HEIGHT, spi, oled_dc, oled_reset, oled_cs)

    def fill(self, *args, **kwargs):
        self.oled.fill(*args, **kwargs)
        self.oled.show()

    def show(self, image: Image.Image):
        self.__restart_display()
        self.oled.image(image)
        self.oled.show()

    def show_text(self, text: str, font_size: int = 10):
        image = Image.new("1", (self.oled.width, self.oled.height))
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("DejaVuSansMono.ttf", font_size)
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (self.oled.width // 2 - font_width // 2, self.oled.height // 2 - font_height // 2),
            text,
            font=font,
            fill=255,
        )
        self.show(image)

    def __reset_oled(self):
        """
        Picture from the display dissappears after around 3-10 seconds randomly. Therefore display must be restarted in
        regular interval to show the picture again.
        Reset of the display takes up to 0.3-0.5 second. That's why the refresh rate can't be too high. Picture is
        blinking.
        On the other hand if the refresh_rate is too high then image may disappear on the begining of time frame and
        will not be visible for the rest of time. Ex. 5 second refresh rate and image disappears in 1st second. The
        remaining 4 seconds screen is empty.
        """
        while True:
            time.sleep(self.REFRESH_RATE)
            temp_buff = bytearray((self.oled.height // 8) * self.oled.width)
            temp_buff[:] = self.oled.buf
            self.__restart_display()
            self.oled.buf[:] = temp_buff
            self.oled.show()

    def __restart_display(self):
        self.oled.poweron()
        self.oled.init_display()
