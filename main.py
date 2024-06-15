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
        self.button_wear = butt.Button("wear", 190, 570)
        self.buttons = [self.button_buy, self.button_eat, self.button_wear]
        # PET DATA -->
        self.pet_main = pet.Pet(530, 200, PET)
        self.pet_game = pet.Pet(650, 550, PET_MINI)
        # INDICATOR DATA -->
        self.happiness = indicator.Indicator(HAPPINESS, 5, 5)
        self.satiety = indicator.Indicator(SATIETY, 5, 145)
        self.health = indicator.Indicator(HEALTH, 5, 285)
        self.money = indicator.Indicator(MONEY, 5, 425)
        self.indicators = [self.happiness, self.satiety, self.health, self.money]
        # MENU INDICATORS -->
        self.bought_top_label_on = indicator.Indicator(TOP_LABEL_ON, 100, 0, "bought")
        self.worn_top_label_on = indicator.Indicator(TOP_LABEL_ON, 100, 100, "worn")
        self.bought_top_label_off = indicator.Indicator(TOP_LABEL_OFF, 100, 0, "didn't buy")
        self.worn_top_label_off = indicator.Indicator(TOP_LABEL_OFF, 100, 100, "taken off")
        # FOOD -->
        self.apple = indicator.Indicator(APPLE, 640, 360, ">>Apple<<")
        self.bone = indicator.Indicator(BONE, 640, 360, ">>Bone<<")
        self.dog_food = indicator.Indicator(DOG_FOOD, 640, 360, ">>Dog Food<<")
        self.dog_food_elite = indicator.Indicator(DOG_FOOD_ELITE, 630, 360, ">>Dog Food Elite<<")
        self.meat = indicator.Indicator(MEAT, 640, 360, ">>Meat<<")
        self.medicine = indicator.Indicator(MEDICINE, 640, 360, ">>Medicine<<")
        self.food = [self.apple, self.bone, self.dog_food, self.dog_food_elite, self.meat, self.medicine]
        # CLOTHES & ITEMS -->
        self.glasses = indicator.Indicator(GLASSES, 630, 360, ">>Cool Glasses<<", "glasses")
        self.sunglasses = indicator.Indicator(SUNGLASSES, 630, 360, ">>Sun Glasses<<", "glasses")
        self.blue_tshirt = indicator.Indicator(BLUE_TSHIRT, 630, 360, ">>blue t-shirt<<", "t-shirt")
        self.red_tshirt = indicator.Indicator(RED_TSHIRT, 630, 360, ">>red t-shirt<<", "t-shirt")
        self.yellow_tshirt = indicator.Indicator(YELLOW_TSHIRT, 630, 360, ">>yellow t-shirt<<", "t-shirt")
        self.boots = indicator.Indicator(BOOTS, 630, 360, ">>cool sneakers<<", "boots")
        self.items = [self.glasses, self.sunglasses, self.blue_tshirt, self.red_tshirt, self.yellow_tshirt, self.boots]
        # TEXT DATA -->
        self.font = FONT
        self.happiness_value = 100
        self.satiety_value = 100
        self.health_value = 100
        self.money_value = 1000
        self.score_value = 0
        self.food_prices = [195, 230, 100, 145, 175, 190]
        self.clothing_prices = [400, 200, 300, 300, 300, 250]
        self.option = 0
        # MINI GAME DATA-->
        self.falling_toys = pg.USEREVENT
        pg.time.set_timer(self.falling_toys, 500)
        self.toys = []
        # OTHER -->
        self.satiety_gone = pg.USEREVENT + 1
        pg.time.set_timer(self.satiety_gone, 3000)
        self.purchased_clothes = []
        self.wear_num = int
        # self.wear_boots_num = int
        # self.wear_glasses_num = int
        # self.wear_tshirt_num = int

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
                        # BUYING CLOTHES -->
                        if button_.text == "buy" and self.current_tub == 2:
                            if self.option not in self.purchased_clothes:
                                if self.money_value >= self.clothing_prices[self.option]:
                                    self.money_value -= self.clothing_prices[self.option]
                                    self.purchased_clothes.append(self.option)
                        # PUTTING ON CLOTHES -->
                        elif button_.text == "wear" and self.current_tub == 2:
                            if self.wear_num != self.option and self.option in self.purchased_clothes:
                                self.wear_num = self.option
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
                    self.pet_game.rect_col.x = 650
                    self.option = 0
            # MINI GAME EVENTS -->
            if self.current_tub == 3:
                key = pygame.key.get_pressed()
                if key[pygame.K_a] is True and self.pet_game.rect.left > 145:
                    self.pet_game.rect.x -= 15
                elif key[pygame.K_d] is True and self.pet_game.rect.right < 1515:
                    self.pet_game.rect.x += 15
                if event.type == self.falling_toys:
                    new_toy = mini_game.FallingToys(random.randint(145, 1100), 50)
                    self.toys.append(new_toy)
            # DECREASED SATIETY -->
            if event.type == self.satiety_gone:
                self.satiety_value -= 1

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

    def render(self):
        self.display.blit(BACKGROUND, [0, 0])
        for button in self.main_buttons:
            button.render(self.display)
        for indicator_ in self.indicators:
            indicator_.render(self.display)
        if self.current_tub == 0:
            self.pet_main.render(self.display)
            # RENDERING OF SELECTED CLOTHES -->
            for wear in range(len(self.items)):
                if wear == self.wear_num:
                    if self.items[wear].text == ">>Cool Glasses<<":
                        self.items[wear].rect = pg.Rect((615, 390), (0, 0))
                    elif self.items[wear].text == ">>Sun Glasses<<":
                        self.items[wear].rect = pg.Rect((530, 328), (0, 0))
                    elif self.items[wear].text in [">>blue t-shirt<<", ">>red t-shirt<<", ">>yellow t-shirt<<"]:
                        self.items[wear].rect = pg.Rect((530, 200), (0, 0))
                    elif self.items[wear].text == ">>cool sneakers<<":
                        self.items[wear].rect = pg.Rect((498, 340), (0, 0))
                    self.items[wear].render(self.display)
        # RENDER OF INSCRIPTIONS -->
        self.font.render_to(self.display, [1300, 125], self.button_food.text, BROWN)
        self.font.render_to(self.display, [1270, 225], self.button_clothe.text, BROWN)
        self.font.render_to(self.display, [1247, 325], self.button_game.text, BROWN)
        self.font.render_to(self.display, [1270, 425], self.button_upgrade.text, BROWN)
        # RENDER VALUES -->
        self.font.render_to(self.display, [180, 100], f"{self.happiness_value}%", BLUE)
        self.font.render_to(self.display, [180, 240], f"{self.satiety_value}%", BLUE)
        self.font.render_to(self.display, [180, 380], f"{self.health_value}%", BLUE)
        self.font.render_to(self.display, [180, 520], f"{self.money_value}$", BLUE)
        # TABS -->
        if self.current_tub != 0:
            # TUB №1 -->
            if self.current_tub == 1:
                self.display.blit(TAB, (0, 0))
                self.button_eat.render(self.display)
                self.font.render_to(self.display, [700, 625], self.button_eat.text, BROWN)
                colour = BROWN if self.money_value >= self.food_prices[self.option] else RED
                self.font.render_to(self.display, [705, 270], str(self.food_prices[self.option]), colour)
                self.font.render_to(self.display, [640, 170], self.food[self.option].text, BROWN)
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
                self.font.render_to(self.display, [250, 592], self.button_wear.text, BROWN)
                self.font.render_to(self.display, [700, 625], self.button_buy.text, BROWN)
                self.font.render_to(self.display, [585, 170], str(self.items[self.option].text), BROWN)
                colour = BROWN if self.money_value >= self.clothing_prices[self.option] else RED
                self.font.render_to(self.display, [705, 270], str(self.clothing_prices[self.option]), colour)
                self.items[self.option].render(self.display)
                self.display.blit(BACK, RECT_BACK)
                self.display.blit(FORWARD, RECT_FORWARD)
                if self.wear_num == self.option:
                    self.worn_top_label_on.render(self.display)
                    self.font.render_to(self.display, [1140, 250], self.worn_top_label_on.text, BROWN)
                else:
                    self.worn_top_label_off.render(self.display)
                    self.font.render_to(self.display, [1088, 250], self.worn_top_label_off.text, BROWN)
                if self.option in self.purchased_clothes:
                    self.bought_top_label_on.render(self.display)
                    self.font.render_to(self.display, [1115, 150], self.bought_top_label_on.text, BROWN)
                else:
                    self.bought_top_label_off.render(self.display)
                    self.font.render_to(self.display, [1088, 150], self.bought_top_label_off.text, BROWN)
            # TAB №3 -->
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
            self.render()


if __name__ == "__main__":
    game = Game()
    game.run()
