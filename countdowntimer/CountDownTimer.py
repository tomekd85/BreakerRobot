import time

from Display.Display import Display

ZERO_TIME = "00:00"


class CountDownTimer:

    def __init__(self, display: Display):
        self.display = display

    def sleep(self, duration, get_now=time.perf_counter):
        now = get_now()
        end = now + duration
        while now < end:
            now = get_now()

    def count(self, time_in_seconds: int):
        font_size = 40
        for sec in range(time_in_seconds, 0, -1):
            ty_sec = time.gmtime(sec)
            text = time.strftime("%M:%S", ty_sec)
            self.sleep(1)
            self.display.show_text(text, font_size, 2)
        self.display.show_text(ZERO_TIME, font_size, 10)
