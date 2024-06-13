from settings import *


class Pet:
    def __init__(self, x, y, image):
        self.image = image
        self.size = PET.get_size()
        self.rect = pg.Rect((x, y), self.size)
        self.rect_col = pg.Rect((self.rect.x, self.rect.y), [x // 2, y // 2])

    def render(self, display):
        display.blit(self.image, self.rect_col)
