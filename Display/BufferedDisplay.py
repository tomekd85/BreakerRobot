from PIL.Image import Image

from Display.Display import Display


class BufferedDisplay(Display):

    def __init__(self):
        self.buffer = ""

    def show_text(self, text: str, font_size: int = 10):
        self.buffer += (text + "|")

    def show(self, image: Image):
        self.buffer += image.filename.split('/')[-1] + "|"

    def get_buffer(self):
        return self.buffer
