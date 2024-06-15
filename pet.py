from settings import *


class Pet:
    def __init__(self, x, y, image):
        self.image = image
        self.size = image.get_size()
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = pg.Rect((x, y), self.size)
        self.rect_col = pg.Rect((x, y), [self.width // 2, self.height // 2])

    def render(self, display):
        display.blit(self.image, self.rect)
        self.rect_col.centerx = self.rect.centerx
        self.rect_col.centery = self.rect.centery
