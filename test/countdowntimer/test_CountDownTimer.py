import time
import unittest

from Display.Display import Display
from countdowntimer.KeyboardInput import KeyboardInput
from countdowntimer.CountDownTimer import CountDownTimer
from Display.BufferedDisplay import BufferedDisplay
from countdowntimer.Observable import Observable


class MyTestCase(unittest.TestCase):
    def test_sleep_works(self):
        CountDownTimer(Display(), KeyboardInput(), 1).sleep(1)
        self.assertEqual(True, True)  # add assertion here

    def test_prints_time_left_every_second(self):
        display = BufferedDisplay()
        CountDownTimer(display, Observable(), 2).count()
        self.assertEqual("buzia1.bmp|buzia3.bmp|", display.get_buffer())

    def test_counter_lasts_the_time_specified(self):
        display = BufferedDisplay()
        duration = 2
        now = time.time()
        CountDownTimer(display).count(duration)
        after = time.time()
        time_lasted = after - now
        epsilon = 0.01
        self.assertTrue(abs(duration - time_lasted) < epsilon,
                        "duration = %s, time_lasted = %s" % (duration, time_lasted))


if __name__ == '__main__':
    unittest.main()
