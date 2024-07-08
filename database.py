import json


class Database:
    def __init__(self, name, keys: list[str]):
        self.name = f"{name}.json"
        self.keys = keys
        try:
            with open(self.name, "r") as json_file:
                self.dict = json.load(json_file)
        except FileNotFoundError:
            self.new_file()
            self.dict = {}

    def check(self, pk):
        return pk in self.dict

    def new_file(self):
        with open(self.name, "w") as json_file:
            json.dump({}, json_file)

    def create(self, record):
        pk = record[0]
        data = dict(zip(self.keys[1:], record[1:]))
        if not self.check(pk):
            self.dict[pk] = data
            self.save()
        else:
            raise ValueError("Record exists")

    def update(self, record):
        pk = record[0]
        data = dict(zip(self.keys[1:], record[1:]))
        if self.check(pk):
            self.dict[pk] = data
            self.save()
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

    def save(self):
        with open(self.name, "w") as json_file:
            json.dump(self.dict, json_file, indent=3)


# player_db = Database("player", ["PlayerID", "indicators", "clothes"])
# player_db.update(["User1", {"satiety": 100, "money": 10000,
#                                                  "happiness": 100, "health": 100},
#                                        {"wear_num": []}])
# # player_db.save()
# # print(player_db.read("User1"))
#
# read_data = player_db.read("User1")
# satiety_value = read_data["indicators"]["satiety"]
# print(satiety_value)
# print(player_db.make_dict())
