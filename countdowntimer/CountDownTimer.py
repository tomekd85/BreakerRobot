import time
from pathlib import Path

from PIL import Image

from Beeper import Beeper
from Display.Display import Display
from countdowntimer.Listener import Listener
from countdowntimer.Observable import Observable

ZERO_TIME = "00:00"


class CountDownTimer(Listener):

    def __init__(self, display: Display, button_observable: Observable, time_in_seconds: int, buzzer: Beeper):
        self.buzzer = buzzer
        self.sec = 0
        self.count_time = time_in_seconds
        self.show_time_seconds = 0
        self.display = display
        self.text = ZERO_TIME
        self.currently_displayed_name = None
        self.button_observable = button_observable
        self.button_observable.register(self)
        self.button_observable.start()

    def sleep(self, duration, get_now=time.perf_counter):
        now = get_now()
        end = now + duration
        while now < end:
            now = get_now()

    def count(self):
        self.sec = self.count_time
        while True:
            to_display = self.get_to_display()
            to_display = self.display_time_conditionally(to_display)
            self.show_on_display(to_display)
            self.sleep(1)
            if self.sec == 1:
                self.buzzer.beep(0.8)
            if self.sec > 0:
                self.sec -= 1

    def display_time_conditionally(self, to_display):
        if self.show_time_seconds > 0:
            to_display = self.setup_text_display(self.sec)
            self.show_time_seconds -= 1
        return to_display

    def get_to_display(self):
        moment_in_break = self.sec / self.count_time
        if moment_in_break > 0.2:
            to_display = "buzia1.bmp"
        elif 0.2 >= moment_in_break > 0:
            to_display = "buzia2.bmp"
        else:
            to_display = "buzia3.bmp"
        return to_display

    def setup_text_display(self, sec):
        time_left = time.gmtime(sec)
        self.text = time.strftime("%M:%S", time_left)
        return self.text

    def show_on_display(self, to_display):
        if to_display != self.currently_displayed_name:
            if self.text == to_display:
                self.display.show_text(to_display, 40)
            else:
                self.display.show(self.load_image(to_display))
            self.currently_displayed_name = to_display

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

    def on_key_press(self, key):
        if key == "B1":
            self.show_time_left()
        if key == "B2":
            self.reset_timer()

    def show_time_left(self):
        self.show_time_seconds = 5
        to_display = self.setup_text_display(self.sec)
        self.show_on_display(to_display)

    def reset_timer(self):
        self.sec = self.count_time

