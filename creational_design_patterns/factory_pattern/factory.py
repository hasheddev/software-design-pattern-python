#single responsibility principle
from math import sin, cos

class Point:
    #factory = PointFactory()
    #make the methods non static or make Factory an inner class
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    p = Point(2, 3)
    p1 = PointFactory.new_polar_point(2, 3)
    p2 = PointFactory.new_cartesian_point(2, 3)
    print(p, "Normal")
    print(p1, "Polar")
    print(p2, "Cartesian")