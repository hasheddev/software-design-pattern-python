class CreatureUnstable:
    def __init__(self) -> None:
        self.strenght = 10
        self.agility = 10
        self.intelligence = 10

    @property
    def total_stats(self):
        return self.strenght + self.intelligence + self.agility

    @property
    def max_stat(self):
        return max(self.strenght, self.intelligence, self.agility)

    @property
    def stat_average(self):
        return self.total_stats / 3.0

class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2
    def __init__(self) -> None:
        self.stats = [10, 10, 10]
        

    @property
    def strenght(self):
        return self.stats[self._strength]

    @strenght.setter
    def strenght(self, value):
        self.stats[self._strength] = value

    @property
    def agility(self):
            return self.stats[self._agility]

    @agility.setter
    def agility(self, value):
        self.stats[self._agility] = value

    @property
    def intelligence(self):
        return self.stats[self._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[self._intelligence] = value

    @property
    def total_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def stat_average(self):
        return float(self.total_stats) / len(self.stats)