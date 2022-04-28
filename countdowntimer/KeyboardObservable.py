from countdowntimer.Listener import Listener
from countdowntimer.Observable import Observable


class KeyboardObservable(Observable):

    def __init__(self):
        self.observers = []

    def register(self, observer: Listener):
        self.observers.append(observer)

    def notify(self, button):
        for observer in self.observers:
            observer.on_key_press(button)

    # def
    #
    #     import keyboard
    #
    #     while True:
    #         if keyboard.read_key() == "p":
    #             print("You pressed p")
    #             break
    #
    #     while True:
    #         if keyboard.is_pressed("q"):
    #             print("You pressed q")
    #             break
    #
    #     keyboard.on_press_key("r", lambda _: print("You pressed r"))
