from abc import abstractmethod

from PIL.Image import Image


class Display:

    def show_text(self, text: str):
        raise NotImplemented

    def show(self, image: Image):
        raise NotImplemented
