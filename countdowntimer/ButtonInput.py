from RPi import GPIO

from countdowntimer.Listener import Listener
from countdowntimer.Observable import Observable

B1_GPIO_NUMBER = 29
B2_GPIO_NUMBER = 31


class ButtonInput(Observable):

    def __init__(self):
        self.observers = []

    def register(self, listener: Listener):
        self.observers.append(listener)

    def notify(self, button):
        for observer in self.observers:
            observer.on_key_press(button)

    def start(self):
        GPIO.add_event_detect(B1_GPIO_NUMBER, GPIO.RISING, callback=(lambda channel: self.notify("B1")), bouncetime=200)
        GPIO.add_event_detect(B2_GPIO_NUMBER, GPIO.RISING, callback=(lambda channel: self.notify("B2")), bouncetime=200)
