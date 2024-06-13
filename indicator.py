from settings import *


class Indicator:
    def __init__(self, image, x, y):
        self.image = image
        self.size = image.get_size()
        self.rect = pg.Rect((x, y), self.size)

    def render(self, display):
        display.blit(self.image, self.rect)
