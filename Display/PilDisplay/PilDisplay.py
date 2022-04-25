from PIL import Image

from Display.Display import Display


class PilDisplay(Display):

    def show(self, image: Image, refresh_rate=3):
        image.show()

    def show_text(self, text: str, font_size: int = 10, refresh_rate=3):
        pass
