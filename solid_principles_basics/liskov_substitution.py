#For an interface that takes a base class using a derived class should have not affect the effect of the interface 
from abc import ABC, abstractmethod

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width


    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height
    

    def __str__(self) -> str:
        return f"Rectangle {self.width} by {self.height}"

class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value
   
def use_shape(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f"Expected {expected} got {rc.area}")

rc = Rectangle(2, 2)
use_shape(rc)

sq = Square(5)
use_shape(sq)


class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        pass

class RectangleN(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

class SquareN(Shape):
    def __init__(self, side: float):
        self.side = side

    @property
    def area(self) -> float:
        return self.side ** 2

def print_area(shape: Shape):
    print(f"Area: {shape.area}")  # Works reliably for both!
