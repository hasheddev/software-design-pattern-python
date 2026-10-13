class Game:
    def __init__(self):
        self.rats = []


class Rat:
    def __init__(self, game: Game):
        self.game = game
        self.game.rats.append(self)

    @property
    def attack(self):
        return len(self.game.rats)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.game.rats.remove(self)