import pygame as pg

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550


def load_image(name, size):
    load = pg.image.load(name)
    load = pg.transform.scale(load, size)
    return load


BUTTON = load_image("images/button.png", [100, 100])
BUTTON_CLICKED = load_image("images/button_clicked.png", [100, 100])
BACKGROUND = load_image("images/background.png", [SCREEN_WIDTH, SCREEN_HEIGHT])
