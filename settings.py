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

TOP_LABEL_ON = load_image("images/menu/top_label_on.png", (1400, 700))
TOP_LABEL_OFF = load_image("images/menu/top_label_off.png", (1400, 700))

# TOYS -->
BALL = load_image("images/toys/ball.png", (100, 100))
BLUE_BONE = load_image("images/toys/blue_bone.png", (100, 100))
RED_BONE = load_image("images/toys/red_bone.png", (100, 100))

# COLOURS-->
BROWN = [82, 45, 20]
BLUE = [3, 40, 230]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GOLD = [255, 215, 0]
GREEN = [0, 255, 0]

FONT_50 = pygame.freetype.Font("fonts/main_font.ttf", 50)
FONT_100 = pygame.freetype.Font("fonts/main_font.ttf", 100)
FPS = 60
GO = load_image("images/go_1.PNG", (200, 200))

# FOOD -->
APPLE = load_image("images/food/apple.png", (200, 200))
BONE = load_image("images/food/bone.png", (200, 200))
DOG_FOOD = load_image("images/food/dog_food.png", (200, 200))
DOG_FOOD_ELITE = load_image("images/food/dog_food_elite.png", (200, 200))
MEAT = load_image("images/food/meat.png", (200, 200))
MEDICINE = load_image("images/food/medicine.png", (200, 200))

# CLOTHES & ITEMS -->
GLASSES = load_image("images/glasses.png", (200, 150))
SUNGLASSES = load_image("images/items/sunglasses.png", (350, 300))
BLUE_TSHIRT = load_image("images/items/blue t-shirt.png", (350, 600))
RED_TSHIRT = load_image("images/items/red t-shirt.png", (350, 600))
YELLOW_TSHIRT = load_image("images/items/yellow t-shirt.png", (350, 600))
BOOTS = load_image("images/items/boots.png", (410, 410))

# Default -->
DEFAULT_SET = [100, 10000, 100, 100]
