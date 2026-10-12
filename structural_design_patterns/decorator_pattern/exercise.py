class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    return f"A circle of radius {self.radius}"

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    return f"A square with side {self.side}"


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    func = getattr(self.shape, 'resize', None)
    if callable(func):
      self.shape.resize(factor)

  def __str__(self):
    return f"{self.shape} has the color {self.color}"