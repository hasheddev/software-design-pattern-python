#Hierarchy class
from abc import ABC, abstractmethod
from enum import Enum, auto

class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print("Tea is delicious")


class Coffee(HotDrink):
    def consume(self):
        print("Coffee is delicious")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount) -> HotDrink:
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Tea bag in cup, boil water, pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"grind beans in cup, boil water, pour {amount}ml, enjoy")
        return Coffee()



def make_drink(type: str) -> HotDrink | None:
    if type == "tea":
        return TeaFactory().prepare(200)
    if type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        return None



class HotDrinkMachine:
    class AvailableDrink(Enum):
       COFFEE = auto()
       TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available drinks: ")
        for f in self.factories:
            print(f[0])
        s = input(f"please pick drink(0-{len(self.factories) - 1}):  ")
        idx = int(s)
        s = input('Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)

if __name__ == "__main__":
    # entry = input("What kind of drink would you like? (tea or coffee):  te").lower()

    # drink = make_drink(entry)
    # if drink is not None:
    #     drink.consume()
    hdm = HotDrinkMachine()
    hdm.make_drink()