from settings import *
import random


class FallingToys:
    def __init__(self, x, y):
        self.image1 = BALL
        self.image2 = BLUE_BONE
        self.image3 = RED_BONE
        width = self.image1.get_width()
        height = self.image1.get_height()
        self.rect = pygame.Rect([x, y], [width, height])
        self.speed_y = random.randint(8, 12)
        self.rect_col = pygame.Rect([x, y], [width // 2, height // 2])
        self.image = random.choice([self.image1, self.image2, self.image3])

    def render(self, display):
        display.blit(self.image, self.rect)

    def movement(self):
        self.rect.y += self.speed_y
        self.rect_col.centerx = self.rect.centerx
        self.rect_col.centery = self.rect.centery
