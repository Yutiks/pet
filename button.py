from settings import *


class Button:
    def __init__(self, text, x, y,):
        self.image = BUTTON
        self.image_2 = BUTTON_CLICKED
        self.size = BUTTON.get_size()
        self.text = text
        self.rect = pg.Rect((x, y), self.size)

    def render(self, display):
        display.blit(self.image, self.rect)
