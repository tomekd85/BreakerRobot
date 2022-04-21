import time
import unittest

from Display.Display import Display
from countdowntimer.CountDownTimer import CountDownTimer
from Display.BufferedDisplay import BufferedDisplay


class MyTestCase(unittest.TestCase):
    def test_sleep_works(self):
        CountDownTimer(Display()).sleep(1)
        self.assertEqual(True, True)  # add assertion here

    def test_prints_time_left_every_second(self):
        display = BufferedDisplay()
        CountDownTimer(display).count(2)
        self.assertEqual("00:0200:0100:00", display.get_buffer())

    def test_counter_lasts_the_time_specified(self):
        display = BufferedDisplay()
        duration = 2
        now = time.time()
        CountDownTimer(display).count(duration)
        after = time.time()
        time_lasted = after - now
        epsilon = 0.0001
        self.assertTrue(abs(duration - time_lasted) < epsilon,
                        "duration = %s, time_lasted = %s" % (duration, time_lasted))


if __name__ == '__main__':
    unittest.main()
