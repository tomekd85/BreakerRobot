from threading import Thread

from Beeper import Beeper
import RPi.GPIO as GPIO
from time import sleep


class RpiBeeper(Beeper):

    def __init__(self, gpio_port=21):
        self.gpio_port = gpio_port
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_port, GPIO.OUT)

    def beep(self, time):
        def make_beep(duration):
            GPIO.output(self.gpio_port, GPIO.HIGH)
            sleep(duration)
            GPIO.output(self.gpio_port, GPIO.LOW)

        beep_thread = Thread(target=make_beep, args=(time,), daemon=True)
        beep_thread.start()
