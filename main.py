import button as butt
from settings import *

# Инициализация pg
pg.init()


# Размеры окна


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.button_food = butt.Button(BUTTON_CLICKED, BUTTON, "food", 100, 100)
        self.button_clothe = butt.Button(BUTTON_CLICKED, BUTTON, "clothe", 200, 100)
        self.button_game = butt.Button(BUTTON_CLICKED, BUTTON, "mini game", 300, 100)
        self.button_upgrade = butt.Button(BUTTON_CLICKED, BUTTON, "upgrade", 400, 100)
        self.buttons = [self.button_food, self.button_clothe, self.button_game, self.button_upgrade]
        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.rect.collidepoint(event.pos):
                        print("clicked")


    def update(self):
        ...

    def draw(self):
        self.screen.blit(BACKGROUND, [0, 0])
        for button in self.buttons:
            button.render(self.screen)
        pg.display.flip()


if __name__ == "__main__":
    Game()
