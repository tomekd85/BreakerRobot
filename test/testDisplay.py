from PIL.Image import Image

from Display.Display import Display


class TestDisplay(Display):

    def __init__(self):
        self.buffer = ""

    def show_text(self, text: str):
        self.buffer += text

    def show(self, image: Image):
        return super().show(image)

    def get_buffer(self):
        return self.buffer