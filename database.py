class Database:
    def __init__(self, name, keys: list[str]):
        self.name = name
        self.keys = keys
        try:
            self.old_file()
            with open(self.name, "r"):
                pass
        except FileNotFoundError:
            self.new_file()

        self.dict = self.make_dict()

    def check(self, pk):
        return pk in self.dict

    def new_file(self):
        main = open(self.name, "w")
        for key in self.keys:
            main.write(f"{key}/")
        main.write("\n")
        main.close()

    def old_file(self):
        pass

    def create(self, inf):
        if not self.check(inf[0]):
            self.dict[inf[0]] = dict(self.connect_keys(inf))
        else:
            raise ValueError("Record exists")

    def update(self, inf):
        if self.check(inf[0]):
            self.dict[inf[0]] = dict(self.connect_keys(inf))
        else:
            raise ValueError("Record not found")

    def read(self, pk):
        if self.check(pk):
            return self.dict[pk]
        raise ValueError("Record not found")

    def connect_keys(self, values):
        connected_list = []
        for i in range(1, len(self.keys)):
            connected_list.append((self.keys[i], values[i]))
        return connected_list

    def make_dict(self):
        the_dict = {}
        main = open(self.name, "r")
        lines = main.readlines()
        main.close()
        for i in lines[1:]:
            value = i.split("/")
            the_dict[value[0]] = dict(self.connect_keys(value))
        return the_dict

    def save(self):
        with open(self.name, "r") as main:
            lines = main.readlines()
        with open(self.name, "w") as main:
            main.write(lines[0])
            for j in self.dict:
                main.write(f"{j}/")
                for i in range(1, len(self.keys)):
                    main.write(f"{self.dict[j][self.keys[i]]}/")
                main.write("\n")


# cars_db = Database("cars.text", ["number-plate", "car-make", "model", "release-date"])
# cars_db.create(["kz-374vaz-01", "BMW", "M5 Competition", "2017"])
# cars_db.create(["kz-001AAA-02", "Mercedes", "GT 63 S", "2018"])
# cars_db.update(["kz-577ASA-14", "Range Rover", "Sport L494", "2022"])
# print(cars_db.dict)
# print(cars_db.read("kz-577ASA-14"))
# cars_db.save()

player_db = Database("player.text", ["PlayerID", "satiety", "money", "happiness", "health"])
# player_db.create(["User1", 100, 10000, 100, 100])
# player_db.update(["User1", 100, 10000, 100, 100])
# player_db.save()
# print(player_db.read("User1"))
# print(player_db.make_dict())
