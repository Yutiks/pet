from settings import *


class Database:
    def __init__(self, name, keys: list[str]):
        self.name = name
        self.keys = keys
        main = open(name, "r")
        lines = main.readlines()
        main.close()
        if not lines:
            main = open(name, "w")
            for key in keys:
                main.write(f"{key}/")
            main.write("\n")
            main.close()

    def create(self, inf):
        main = open(self.name, "a")
        for i in inf:
            main.write(f"{i}/")
        main.write("\n")
        main.close()

    def update(self, inf):
        main = open(self.name, "w")
        for key in self.keys:
            main.write(f"{key}/")
        main.write("\n")
        for item in inf:
            main.write(f"{item}/")
        main.close()

    def read(self):
        main = open(self.name, "r")
        lines = main.readlines()
        main.close()
        if len(lines) > 1:
            data = lines[1].split("/")
            for i in range(len(data)):
                if data[i] == '':
                    data.remove('')
            return list(map(int, data))
        else:
            return DEFAULT_SET
