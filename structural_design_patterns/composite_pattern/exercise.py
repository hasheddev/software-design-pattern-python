from collections.abc import Iterable
from abc import ABC

class Summable(Iterable, ABC):
    @property
    def sum(self):
        total = 0
        for value in self:
            if isinstance(value, int) or isinstance(value, float):
                total += value
            else:
                total += value.sum
        return total

class SingleValue(Summable):
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        yield self.value

class ManyValues(list, Summable):
    def __init__(self):
        super().__init__()