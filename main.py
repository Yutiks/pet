import random

from mini_game import FallingToys
from pet import Pet
from button import Button
from database import Database
from indicator import Indicator
from settings import *

pg.init()


class Game:
    def __init__(self):
        # GAME DATA -->
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Pet")
        self.current_tub = 0
        self.clock = pg.time.Clock()
        # BUTTON DATA -->
        self.button_food = Button("food", 1235, 100)
        self.button_clothe = Button("clothes", 1235, 200)
        self.button_game = Button("mini game", 1235, 300)
        self.button_upgrade = Button("upgrade", 1235, 400)
        self.main_buttons = [self.button_food, self.button_clothe, self.button_game, self.button_upgrade]
        self.button_buy = Button("buy", 618, 600)
        self.button_eat = Button("eat", 618, 600)
        self.button_wear = Button("wear", 190, 570)
        self.buttons = [self.button_buy, self.button_eat, self.button_wear]
        # PET DATA -->
        self.pet_main = Pet(530, 200, PET)
        self.pet_mini = Pet(650, 550, PET_MINI)
        # INDICATOR DATA -->
        self.happiness = Indicator(HAPPINESS, 5, 5)
        self.satiety = Indicator(SATIETY, 5, 145)
        self.health = Indicator(HEALTH, 5, 285)
        self.money = Indicator(MONEY, 5, 425)
        self.indicators = [self.happiness, self.satiety, self.health, self.money]
        # MENU INDICATORS -->
        self.bought_top_label_on = Indicator(TOP_LABEL_ON, 100, 0, "bought")
        self.worn_top_label_on = Indicator(TOP_LABEL_ON, 100, 100, "worn")
        self.bought_top_label_off = Indicator(TOP_LABEL_OFF, 100, 0, "didn't buy")
        self.worn_top_label_off = Indicator(TOP_LABEL_OFF, 100, 100, "taken off")
        # FOOD -->
        self.apple = Indicator(APPLE, 640, 360, ">>Apple<<")
        self.bone = Indicator(BONE, 640, 360, ">>Bone<<")
        self.dog_food = Indicator(DOG_FOOD, 640, 360, ">>Dog Food<<")
        self.dog_food_elite = Indicator(DOG_FOOD_ELITE, 630, 360, ">>Dog Food Elite<<")
        self.meat = Indicator(MEAT, 640, 360, ">>Meat<<")
        self.medicine = Indicator(MEDICINE, 640, 360, ">>Medicine<<")
        self.food = [self.apple, self.bone, self.dog_food, self.dog_food_elite, self.meat, self.medicine]
        # TEXT DATA -->
        self.font_50 = FONT_50
        self.font_100 = FONT_100
        self.score_value = 0
        self.food_prices = (195, 230, 100, 145, 175, 190)
        self.clothing_prices = (400, 200, 300, 300, 300, 250)
        self.option = 0
        # MINI GAME DATA-->
        self.falling_toys = pg.USEREVENT
        pg.time.set_timer(self.falling_toys, 500)
        self.toys = []
        # OTHER -->
        self.satiety_gone = pg.USEREVENT + 1
        pg.time.set_timer(self.satiety_gone, 3000)
        self.timer = 0
        # DataBase -->
        self.player_db = Database("player", ["PlayerID", "indicators", "clothes"])
        read_data = self.player_db.read("User1")
        self.satiety_value = read_data["indicators"]["satiety"]
        self.money_value = read_data["indicators"]["money"]
        self.happiness_value = read_data["indicators"]["happiness"]
        self.health_value = read_data["indicators"]["health"]
        # CLOTHES & ITEMS (DataBase) -->
        self.purchased_clothes = read_data["clothes"]["purchased_clothes"]
        self.worn = read_data["clothes"]["worn"]
        self.glasses = Indicator(GLASSES, 630, 360, ">>Cool Glasses<<", "glasses",
                                 self.worn[">>Cool Glasses<<"])
        self.sunglasses = Indicator(SUNGLASSES, 630, 360, ">>Sun Glasses<<", "glasses",
                                    self.worn[">>Sun Glasses<<"])
        self.blue_tshirt = Indicator(BLUE_TSHIRT, 630, 360, ">>blue t-shirt<<", "t-shirt",
                                     self.worn[">>blue t-shirt<<"])
        self.red_tshirt = Indicator(RED_TSHIRT, 630, 360, ">>red t-shirt<<", "t-shirt",
                                    self.worn[">>red t-shirt<<"])
        self.yellow_tshirt = Indicator(YELLOW_TSHIRT, 630, 360, ">>yellow t-shirt<<", "t-shirt",
                                       self.worn[">>yellow t-shirt<<"])
        self.boots = Indicator(BOOTS, 630, 360, ">>cool sneakers<<", "boots", self.worn[">>cool sneakers<<"])
        self.items = [self.glasses, self.sunglasses, self.blue_tshirt, self.red_tshirt, self.yellow_tshirt, self.boots]

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.player_db.update(["User1", {"satiety": self.satiety_value, "money": self.money_value,
                                                 "happiness": self.happiness_value, "health": self.health_value},
                                       {"purchased_clothes": self.purchased_clothes, "worn": self.worn}])
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
                        # BUYING CLOTHES -->
                        if button_.text == "buy" and self.current_tub == 2:
                            if not self.purchased_clothes[self.items[self.option].text]:
                                if self.money_value >= self.clothing_prices[self.option]:
                                    self.money_value -= self.clothing_prices[self.option]
                                    self.purchased_clothes[self.items[self.option].text] = True
                        # PUTTING ON CLOTHES -->
                        elif button_.text == "wear" and self.current_tub == 2:
                            if (not self.items[self.option].worn
                                    and self.purchased_clothes[self.items[self.option].text]):
                                self.worn[self.items[self.option].text] = True
                                self.items[self.option].worn = self.worn[self.items[self.option].text]
                                for wear in self.items:
                                    if wear.worn:
                                        if wear != self.items[self.option]:
                                            if wear.type == self.items[self.option].type:
                                                self.worn[wear.text] = False
                                                wear.worn = self.worn[wear.text]
                        # BUYING FOOD -->
                        elif button_.text == "eat" and self.current_tub == 1:
                            if self.money_value >= self.food_prices[self.option]:
                                self.money_value -= self.food_prices[self.option]
                                self.satiety_value += 10
                                if self.satiety_value > 100:
                                    self.satiety_value = 100
                # SWITCH BETWEEN OPTIONS -->
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
                # CLICKER -->
                if self.pet_main.rect_col.collidepoint(event.pos) and self.current_tub == 0:
                    self.money_value += 10
                # EXIT TAB -->
                elif RECT_EXIT.collidepoint(event.pos) and self.current_tub != 0:
                    self.current_tub = 0
                    self.score_value = 0
                    self.toys = []
                    self.pet_mini.rect_col.x = 650
                    self.option = 0
                    self.timer = 0
            # MINI GAME EVENTS -->
            if self.current_tub == 3:
                key = pygame.key.get_pressed()
                if event.type == self.falling_toys:
                    if self.timer <= 4:
                        self.timer += 1
                    else:
                        new_toy = FallingToys(random.randint(145, 1100), 50)
                        self.toys.append(new_toy)
                if self.timer in [4, 5]:
                    if key[pygame.K_a] is True and self.pet_mini.rect.left > 145:
                        self.pet_mini.rect.x -= 15
                    elif key[pygame.K_d] is True and self.pet_mini.rect.right < 1515:
                        self.pet_mini.rect.x += 15

            # DECREASED SATIETY -->
            if event.type == self.satiety_gone:
                self.satiety_value -= 1

    def update(self):
        if self.current_tub == 3:
            for toy in self.toys:
                toy.movement()
                if toy.rect.colliderect(self.pet_mini.rect_col):
                    self.score_value += 1
                    self.toys.remove(toy)
                elif toy.rect.y > 750:
                    if toy in self.toys:
                        self.toys.remove(toy)

    def render(self):
        self.display.blit(BACKGROUND, [0, 0])

        for button in self.main_buttons:
            button.render(self.display)
        for indicator_ in self.indicators:
            indicator_.render(self.display)
        if self.current_tub == 0:
            self.pet_main.render(self.display)
            # RENDERING OF SELECTED CLOTHES -->
            self.items[0].rect = pg.Rect((615, 390), (0, 0))
            self.items[1].rect = pg.Rect((530, 328), (0, 0))
            self.items[2].rect = pg.Rect((530, 200), (0, 0))
            self.items[3].rect = pg.Rect((530, 200), (0, 0))
            self.items[4].rect = pg.Rect((530, 200), (0, 0))
            self.items[5].rect = pg.Rect((498, 340), (0, 0))
            for clothe in self.items:
                if clothe.worn == 1:
                    clothe.render(self.display)
        # RENDER OF INSCRIPTIONS -->
        self.font_50.render_to(self.display, [1300, 125], self.button_food.text, BROWN)
        self.font_50.render_to(self.display, [1270, 225], self.button_clothe.text, BROWN)
        self.font_50.render_to(self.display, [1247, 325], self.button_game.text, BROWN)
        self.font_50.render_to(self.display, [1270, 425], self.button_upgrade.text, BROWN)
        # RENDER VALUES -->
        self.font_50.render_to(self.display, [180, 100], f"{self.happiness_value}%", BLUE)
        self.font_50.render_to(self.display, [180, 240], f"{self.satiety_value}%", BLUE)
        self.font_50.render_to(self.display, [180, 380], f"{self.health_value}%", BLUE)
        self.font_50.render_to(self.display, [180, 520], f"{self.money_value}$", BLUE)
        # TABS -->
        if self.current_tub != 0:
            # TUB №1 -->
            if self.current_tub == 1:
                self.display.blit(TAB, (0, 0))
                self.button_eat.render(self.display)
                self.font_50.render_to(self.display, [700, 625], self.button_eat.text, BROWN)
                colour = BROWN if self.money_value >= self.food_prices[self.option] else RED
                self.font_50.render_to(self.display, [705, 270], str(self.food_prices[self.option]), colour)
                self.font_50.render_to(self.display, [640, 170], self.food[self.option].text, BROWN)
                self.food[self.option].render(self.display)
                self.display.blit(BACK, RECT_BACK)
                self.display.blit(FORWARD, RECT_FORWARD)
            # TAB №2 -->
            elif self.current_tub == 2:
                for right_place in self.items:
                    if right_place.text == ">>Cool Glasses<<":
                        right_place.rect = pg.Rect((640, 400), (0, 0))
                    elif right_place.text == ">>Sun Glasses<<":
                        right_place.rect = pg.Rect((560, 350), (0, 0))
                    elif right_place.text in [">>blue t-shirt<<", ">>red t-shirt<<", ">>yellow t-shirt<<"]:
                        right_place.rect = pg.Rect((560, 120), (0, 0))
                    elif right_place.text == ">>cool sneakers<<":
                        right_place.rect = pg.Rect((530, 160), (0, 0))
                self.display.blit(TAB, (0, 0))
                self.button_buy.render(self.display)
                self.button_wear.render(self.display)
                self.font_50.render_to(self.display, [250, 592], self.button_wear.text, BROWN)
                self.font_50.render_to(self.display, [700, 625], self.button_buy.text, BROWN)
                self.font_50.render_to(self.display, [585, 170], str(self.items[self.option].text), BROWN)
                colour = BROWN if self.money_value >= self.clothing_prices[self.option] else RED
                self.font_50.render_to(self.display, [705, 270], str(self.clothing_prices[self.option]), colour)
                self.items[self.option].render(self.display)
                self.display.blit(BACK, RECT_BACK)
                self.display.blit(FORWARD, RECT_FORWARD)
                if self.items[self.option].worn:
                    self.worn_top_label_on.render(self.display)
                    self.font_50.render_to(self.display, [1140, 250], self.worn_top_label_on.text, BROWN)
                else:
                    self.worn_top_label_off.render(self.display)
                    self.font_50.render_to(self.display, [1088, 250], self.worn_top_label_off.text, BROWN)
                if self.purchased_clothes[self.items[self.option].text]:
                    self.bought_top_label_on.render(self.display)
                    self.font_50.render_to(self.display, [1115, 150], self.bought_top_label_on.text, BROWN)
                else:
                    self.bought_top_label_off.render(self.display)
                    self.font_50.render_to(self.display, [1088, 150], self.bought_top_label_off.text, BROWN)
            # TAB №3 -->
            elif self.current_tub == 3:
                self.display.blit(GAME_BACKGROUND, (0, 0))

                self.pet_mini.render(self.display)
                if self.timer <= 3:
                    self.font_100.render_to(self.display, [675, 328], f"{str(self.timer)}...", BROWN)
                if self.timer == 4:
                    self.display.blit(GO, (600, 250))
                else:
                    for toy_ in self.toys:
                        toy_.render(self.display)
                self.font_50.render_to(self.display, [175, 128], f"score: {str(self.score_value)}", BROWN)
            self.display.blit(EXIT_LOGO, RECT_EXIT)

        pg.display.flip()

    def run(self):
        self.clock.tick(FPS)
        while True:
            self.events()
            self.update()
            self.render()


if __name__ == "__main__":
    game = Game()
    game.run()
