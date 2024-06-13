import pygame as pg
import pygame.freetype
pg.init()


def load_image(name, size):
    load = pg.image.load(name)
    load = pg.transform.scale(load, size)
    return load


# DISPLAY-->
WIDTH = 1475
HEIGHT = 900

# BACKGROUNDS -->
BACKGROUND = load_image("images/background.png", (WIDTH, HEIGHT))
GAME_BACKGROUND = load_image("images/game_background.png", (WIDTH, HEIGHT))
TAB = load_image("images/menu/menu_page.png", (WIDTH, HEIGHT))

# BUTTONS -->
BUTTON = load_image("images/button.png", [230, 80])
BUTTON_CLICKED = load_image("images/button_clicked.png", [230, 80])
EXIT_LOGO = load_image("images/exit.PNG", (50, 50))
BACK = load_image("images/back.PNG", (130, 130))
FORWARD = load_image("images/forward.PNG", (130, 130))

# RECTS -->
RECT_EXIT = pg.Rect([137, 92], EXIT_LOGO.get_size())
RECT_BACK = pg.Rect([155, 660], BACK.get_size())
RECT_FORWARD = pg.Rect([1200, 660], FORWARD.get_size())

# PET -->
PET_SIZE_X = 350
PET_SIZE_Y = 600
PET = load_image("images/dog.png", (PET_SIZE_X, PET_SIZE_Y))
PET_MINI = load_image("images/dog.png", (PET_SIZE_X // 2, PET_SIZE_Y // 2))

# INDICATORS -->
HAPPINESS = load_image("images/happiness.png", (200, 200))
HEALTH = load_image("images/health.png", (200, 200))
MONEY = load_image("images/money.png", (200, 200))
SATIETY = load_image("images/satiety.png", (200, 200))

# ITEMS -->
GLASSES = load_image("images/glasses.png", (200, 150))
SUNGLASSES = load_image("images/items/sunglasses.png", (200, 150))

# TOYS -->
BALL = load_image("images/toys/ball.png", (100, 100))
BLUE_BONE = load_image("images/toys/blue_bone.png", (100, 100))
RED_BONE = load_image("images/toys/red_bone.png", (100, 100))

# COLOURS-->
BROWN = [82, 45, 20]
BLUE = [3, 40, 230]
BLACK = [0, 0, 0]

FONT = pygame.freetype.Font("fonts/main_font.ttf", 50)
FPS = 60
