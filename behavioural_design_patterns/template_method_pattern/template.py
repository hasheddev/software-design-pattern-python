from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Player {self.winning_player} wins")

    @abstractmethod
    def start(self):
        pass

    @property
    @abstractmethod
    def have_winner(self) -> bool:
        pass

    @abstractmethod
    def take_turn(self):
        pass

    @property
    @abstractmethod
    def winning_player(self) -> int:
        pass

class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.turn = 1
        self.max_turns = 10

    def start(self):
        print(f"Starting a game of chess with {self.number_of_players} players")

    @property
    def have_winner(self):
        return self.turn == self.max_turns

    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


if __name__ == "__main__":
    chess = Chess()
    chess.run()