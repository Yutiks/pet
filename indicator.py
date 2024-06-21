from settings import *


class Indicator:
    def __init__(self, image, x, y, text=None, type_=None, worn=None):
        self.image = image
        self.size = image.get_size()
        self.rect = pg.Rect((x, y), self.size)
        self.text = text
        self.type = type_
        self.worn = worn

    def render(self, display):
        display.blit(self.image, self.rect)
