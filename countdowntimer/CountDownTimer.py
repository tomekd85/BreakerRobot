import time
from pathlib import Path

from PIL import Image

from Display.Display import Display

ZERO_TIME = "00:00"


class CountDownTimer:

    def __init__(self, display: Display):
        self.display = display
        self.text = ZERO_TIME

    def sleep(self, duration, get_now=time.perf_counter):
        now = get_now()
        end = now + duration
        while now < end:
            now = get_now()

    def count(self, time_in_seconds: int):
        font_size = 40
        for sec in range(time_in_seconds, 0, -1):
            time_left = time.gmtime(sec)
            self.text = time.strftime("%M:%S", time_left)
            if sec/time_in_seconds > 0.2:
                self.display.show(self.load_smile1())
            else:
                self.display.show(self.load_smile2())
            # self.display.show_text(self.text, font_size)
            self.sleep(1)
        self.text = ZERO_TIME
        self.display.show(self.load_smile3())

    def load_smile1(self) -> Image:
        return self.load_image('buzia1.bmp')

    def load_smile2(self) -> Image:
        return self.load_image('buzia2.bmp')

    def load_smile3(self) -> Image:
        return self.load_image('buzia3.bmp')

    def load_image(self, image_file_name):
        img_path = str(Path(__file__).resolve().parent.joinpath('images', image_file_name))
        smile = Image.open(img_path)
        return smile

