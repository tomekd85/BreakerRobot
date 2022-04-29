from threading import Thread

from pynput import keyboard
from pynput.keyboard import KeyCode

from countdowntimer.ButtonInput.ButtonInput import ButtonInput
from countdowntimer.Listener import Listener
from countdowntimer.Observable import Observable


class KeyboardInput(ButtonInput, Observable):

    def __init__(self):
        self.observers = []

    def register(self, listener: Listener):
        self.observers.append(listener)

    def notify(self, button):
        for observer in self.observers:
            observer.on_key_press(button)

    def button_pressed(self, button: KeyCode) -> None:
        if button.char == 'a':
            self.notify("B1")
        if button.char == 'b':
            self.notify("B2")

    def start(self):
        t = Thread(target=self.run, daemon=True)
        t.start()

    def run(self):
        def on_press(key):
            try:
                print('Alphanumeric key pressed: {0} '.format(
                    key.char))
                self.button_pressed(key)
            except AttributeError:
                print('special key pressed: {0}'.format(
                    key))

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
