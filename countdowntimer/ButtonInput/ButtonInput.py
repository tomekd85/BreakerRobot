from pynput.keyboard import KeyCode


class ButtonInput:
    def button_pressed(self, button: KeyCode) -> str:
        raise NotImplementedError

    def start(self):
        raise NotImplementedError
