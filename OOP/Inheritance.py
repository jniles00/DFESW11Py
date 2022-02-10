from unicodedata import name


class athlete:
    def __init__(self, name):
        self.name = name

class footballer(athlete):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team


player1 = footballer("Jay", "Droylsen FC")