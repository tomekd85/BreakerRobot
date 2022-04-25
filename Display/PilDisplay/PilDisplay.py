from PIL import Image

from Display.Display import Display


class PilDisplay(Display):

    def show(self, image: Image):
        image.show()

    def show_text(self, text: str):
        pass
