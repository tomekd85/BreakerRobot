from abc import abstractmethod

from PIL.Image import Image


class Display:

    def show_text(self, text: str, font_size: int = 10, refresh_rate: float = 3):
        raise NotImplemented

    def show(self, image: Image, refresh_rate: float = 3):
        raise NotImplemented
