import button as butt
from settings import *
import pet
import indicator
import mini_game
import random
pg.init()


class Game:
    def __init__(self):
        # GAME DATA -->
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Pet")
        self.current_tub = 0
        self.clock = pg.time.Clock()
        # BUTTON DATA -->
        self.button_food = butt.Button("food", 1235, 100)
        self.button_clothe = butt.Button("clothes", 1235, 200)
        self.button_game = butt.Button("mini game", 1235, 300)
        self.button_upgrade = butt.Button("upgrade", 1235, 400)
        self.main_buttons = [self.button_food, self.button_clothe, self.button_game, self.button_upgrade]
        self.button_buy = butt.Button("buy", 618, 600)
        self.button_eat = butt.Button("eat", 618, 600)
        self.buttons = [self.button_buy, self.button_eat]
        # PET DATA -->
        self.pet_main = pet.Pet(530, 200, PET)
        self.pet_game = pet.Pet(650, 550, PET_MINI)
        # INDICATOR DATA -->
        self.happiness = indicator.Indicator(HAPPINESS, 5, 5)
        self.satiety = indicator.Indicator(SATIETY, 5, 145)
        self.health = indicator.Indicator(HEALTH, 5, 285)
        self.money = indicator.Indicator(MONEY, 5, 425)
        self.indicators = [self.happiness, self.satiety, self.health, self.money]
        # TEXT DATA -->
        self.font = FONT
        self.happiness_value = 100
        self.satiety_value = 100
        self.health_value = 100
        self.money_value = 0
        self.score_value = 0
        self.food_prices = [199, 230, 60]
        self.clothing_prices = [80, 40, 200]
        self.option = 0
        # MINI GAME DATA-->
        self.falling_toys = pg.USEREVENT
        pg.time.set_timer(self.falling_toys, 500)
        self.toys = []

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                for button in self.main_buttons:
                    if button.rect.collidepoint(event.pos) and self.current_tub == 0:
                        if button.text == "food":
                            self.current_tub = 1
                        elif button.text == "clothes":
                            self.current_tub = 2
                        elif button.text == "mini game":
                            self.current_tub = 3
                        elif button.text == "upgrade":
                            print("upgrade")
                for button_ in self.buttons:
                    if button_.rect.collidepoint(event.pos) and self.current_tub != 0:
                        if button_.text == "buy" and self.current_tub == 2:
                            print("buy")
                        elif button_.text == "eat" and self.current_tub == 1:
                            print("eat")
                if RECT_BACK.collidepoint(event.pos):
                    if self.current_tub in [1, 2]:
                        if self.option - 1 >= 0:
                            self.option -= 1
                elif RECT_FORWARD.collidepoint(event.pos):
                    if self.current_tub == 1:
                        if self.option + 1 < len(self.food_prices):
                            self.option += 1
                    elif self.current_tub == 2:
                        if self.option + 1 < len(self.clothing_prices):
                            self.option += 1

                if self.pet_main.rect.collidepoint(event.pos) and self.current_tub == 0:
                    self.money_value += 10
                elif RECT_EXIT.collidepoint(event.pos) and self.current_tub != 0:
                    self.current_tub = 0
                    self.score_value = 0
                    self.toys = []
                    self.pet_game.rect_col.x = 650
                    self.option = 0
            if self.current_tub == 3:
                key = pygame.key.get_pressed()
                if key[pygame.K_a] is True and self.pet_game.rect_col.left > 145:
                    self.pet_game.rect_col.x -= 10
                elif key[pygame.K_d] is True and self.pet_game.rect_col.right < 1515:
                    self.pet_game.rect_col.x += 10
                if event.type == self.falling_toys and self.current_tub == 3:
                    new_toy = mini_game.FallingToys(random.randint(145, 1100), 50)
                    self.toys.append(new_toy)

    def update(self):
        if self.current_tub == 3:
            for toy in self.toys:
                toy.movement()
                if toy.rect.colliderect(self.pet_game.rect_col):
                    self.score_value += 1
                    self.toys.remove(toy)
                elif toy.rect.y > 750:
                    if toy in self.toys:
                        self.toys.remove(toy)

    def draw(self):
        self.display.blit(BACKGROUND, [0, 0])
        for button in self.main_buttons:
            button.render(self.display)
        for indicator_ in self.indicators:
            indicator_.render(self.display)
        if self.current_tub == 0:
            self.pet_main.render(self.display)
        # RENDER OF INSCRIPTIONS -->
        self.font.render_to(self.display, [1300, 125], self.button_food.text, BROWN)
        self.font.render_to(self.display, [1270, 225], self.button_clothe.text, BROWN)
        self.font.render_to(self.display, [1247, 325], self.button_game.text, BROWN)
        self.font.render_to(self.display, [1270, 425], self.button_upgrade.text, BROWN)
        # RENDER VALUES -->
        self.font.render_to(self.display, [180, 100], str(self.happiness_value), BLUE)
        self.font.render_to(self.display, [180, 240], str(self.satiety_value), BLUE)
        self.font.render_to(self.display, [180, 380], str(self.health_value), BLUE)
        self.font.render_to(self.display, [180, 520], str(self.money_value), BLUE)
        # TABS -->
        if self.current_tub != 0:
            if self.current_tub == 1:
                self.display.blit(TAB, (0, 0))
                self.button_eat.render(self.display)
                self.font.render_to(self.display, [700, 625], self.button_eat.text, BROWN)
                self.font.render_to(self.display, [705, 270], str(self.food_prices[self.option]), BROWN)
                self.display.blit(BACK, RECT_BACK)
                self.display.blit(FORWARD, RECT_FORWARD)
            elif self.current_tub == 2:
                self.display.blit(TAB, (0, 0))
                self.button_buy.render(self.display)
                self.font.render_to(self.display, [700, 625], self.button_buy.text, BROWN)
                self.font.render_to(self.display, [705, 270], str(self.clothing_prices[self.option]), BROWN)
                self.display.blit(BACK, RECT_BACK)
                self.display.blit(FORWARD, RECT_FORWARD)
            elif self.current_tub == 3:
                self.display.blit(GAME_BACKGROUND, (0, 0))
                self.pet_game.render(self.display)
                for toy_ in self.toys:
                    toy_.render(self.display)
                self.font.render_to(self.display, [175, 128], f"score: {str(self.score_value)}", BROWN)
            self.display.blit(EXIT_LOGO, RECT_EXIT)

        pg.display.flip()

    def run(self):
        self.clock.tick(FPS)
        while True:
            self.events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
