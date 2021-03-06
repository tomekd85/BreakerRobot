from RPi import GPIO

from countdowntimer.Listener import Listener
from countdowntimer.Observable import Observable

B1_GPIO_NUMBER = 5
B2_GPIO_NUMBER = 6


class ButtonInput(Observable):

    def __init__(self):
        self.observers = []

    def register(self, listener: Listener):
        self.observers.append(listener)

    def notify(self, button):
        for observer in self.observers:
            observer.on_key_press(button)

    def callback_b1(self, channel):
        self.notify("B1")

    def callback_b2(self, channel):
        self.notify("B2")

    def start(self):
        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
        GPIO.setup([B1_GPIO_NUMBER, B2_GPIO_NUMBER], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(B1_GPIO_NUMBER, GPIO.RISING, callback=self.callback_b1, bouncetime=200)
        GPIO.add_event_detect(B2_GPIO_NUMBER, GPIO.RISING, callback=self.callback_b2, bouncetime=200)

