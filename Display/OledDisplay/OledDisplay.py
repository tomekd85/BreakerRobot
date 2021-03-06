import time
from threading import Thread


from PIL import ImageFont, ImageDraw, Image
import os
if os.uname().machine.startswith("arm"):
    from luma.oled.device import ssd1306
else:
    from luma.emulator.device import pygame
from luma.core.interface.serial import spi

from Display.Display import Display


class OledDisplay(Display):

    def __init__(self):
        self.oled = self.__initialize_oled()

    def __initialize_oled(self):
        if os.uname().machine.startswith("arm"):
            return ssd1306(serial_interface=spi())
        else:
            return pygame()

    def show(self, image: Image.Image):
        self.oled.display(image)

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
