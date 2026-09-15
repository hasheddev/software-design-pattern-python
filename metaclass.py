from typing import Any


class Foo:
    def show(self):
        print("hi")

class TestR:
    pass

def add_sttr(self):
    self.z = 9

class TestN(Foo):
    x = 5
    add_attr = add_sttr

#this is same as above
#TypeObject = type(name, bases, dict)
#name ("Test"): The name of the class.
#bases (Foo,): A tuple of parent classes to inherit from.
#dict {"x": 5, ...}: The attribute/method namespace dictionary for the class body.
Test = type("Test", (Foo,), {"x": 5, "add_attr": add_sttr})
t = Test()
print(t.x)
t.add_attr()
print(t.z)
t.show()
print(type(t))

# / = left side position args only func(1, 2, 3, /)
# * = right side key word only  func(key=val, valu=low)
class Meta(type):
    def __new__(cls, name: str, bases, attrs):
        print(attrs)
        super().__new__(cls, name, bases, attrs)
        return type(name, bases, attrs)

class Dog(metaclass=Meta):
    x = 5
    y = 8

class Bee():
    x = 5
    y = 8
bee = Bee()

print(Bee.x, bee.x)