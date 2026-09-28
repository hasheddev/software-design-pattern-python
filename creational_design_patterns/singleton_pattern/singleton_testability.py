from typing import Any
import unittest

class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        self.population = {}
        with open("capitals.txt", 'r') as f:
            lines = f.readlines()
            for i in range (0, len(lines), 2):
                self.population[lines[i].strip()] = int(lines[i + 1].strip())

class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        db = Database()
        for city in cities:
            result += db.population.get(city, 0)
        return result

class ConfigurableRecordFinder:
    def __init__(self, db=None) -> None:
        database = db if db is not None else Database()
        self.db = database

    def total_population(self, cities):
        result = 0
        for city in cities:
            result += self.db.population.get(city, 0)
        return result

class DummyDatabase:
    population = {"alpha": 1, "beta": 2, "gamma": 3}

    def get_population(self, name):
        return self.population.get(name, 0)
    

class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(17500000 + 17400000, tp)

    def test_dependend_popuation(self):
        ddb = DummyDatabase()
        crf = ConfigurableRecordFinder(ddb)
        self.assertEqual(crf.total_population(['alpha', 'beta']), 3)