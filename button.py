import  pygame as pg


class Button:
    def __init__(self, image_pressed, image_not_pressed, text, x, y,):
        self.image = image_not_pressed
        self.image_2 = image_pressed
        self.size = image_pressed.get_size()
        self.text = text
        self.rect = pg.Rect([x, y], self.size)

    def render(self, display):
        display.blit(self.image, self.rect)
