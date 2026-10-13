from abc import ABC, abstractmethod
from enum import Enum

class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 1

class Query:
    def __init__(self,  what_to_query: WhatToQuery, default_value: int) -> None:
        self.what_to_query = what_to_query
        self.value = default_value

class Creature(ABC):
    def __init__(self, game: "Game", attack: int, defense: int):
        self._attack = attack
        self._defense = defense
        self.game = game
    
    @property
    def attack(self) -> int:
        return self._attack
    
    @property
    def defense(self) -> int:
        return self._defense
    
    @abstractmethod
    def add_bonus(self, source: "Creature", query: Query):
        pass

class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        q = Query(WhatToQuery.ATTACK, self._attack)
        for c in self.game.creatures:
            c.add_bonus(c, q)
        return q.value
        
    @property
    def defense(self):
        q = Query(WhatToQuery.DEFENSE, self._defense)
        return q.value
        
    def add_bonus(self, source, query: Query):
        if self != source and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 1
        
        
class GoblinKing(Goblin):
    def __init__(self, game, attack=3, defense=3):
        super().__init__(game, attack, defense)

    def add_bonus(self, source, query: Query):
        if self != source and query.what_to_query == WhatToQuery.ATTACK:
            query.value += 1
        else:
            super().add_bonus(source, query)

class Game:
    def __init__(self):
        self.creatures: list[Creature] = []