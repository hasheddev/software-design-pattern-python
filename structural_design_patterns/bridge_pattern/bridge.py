from abc import ABC

#circle square
# vector raster

#CircleVector  CircleRaster  SquareVector  SquareRaster

class Renderer(ABC):
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing circle of radius {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixel for circle of radius {radius}")


class Shape:
    def __init__(self, renderer) -> None:
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass

class Circle(Shape):
    def __init__(self, renderer, radius) -> None:
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
       self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self. radius *= factor

if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
