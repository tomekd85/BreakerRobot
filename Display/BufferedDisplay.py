from PIL.Image import Image

from Display.Display import Display


class BufferedDisplay(Display):

    def __init__(self):
        self.buffer = ""

    def show_text(self, text: str, font_size=10, refresh_rate=3):
        self.buffer += text

    def show(self, image: Image, refresh_rate=3):
        self.buffer += repr(image)

    def get_buffer(self):
        return self.buffer
