#when api does not match what you work with

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)

def draw_point(p):
    print('.', end='')

class Line:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __hash__(self):
        return hash((self.start, self.end))

    def __eq__(self, other):
        return isinstance(other, Line) and (self.start, self.end) == (other.start, other.end)


class Rectangle(list):
    def __init__(self, x, y, width, height) -> None:
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))

class LineToPointAdapter:
    cache = {}

    def __init__(self, line):
        self.h = hash(line)
        
        if self.h not in self.cache:
            print(f"Generating points for line [{line.start.x}, {line.start.y}] => [{line.end.x}, {line.end.y}]")
            
            left = min(line.start.x, line.end.x)
            right = max(line.start.x, line.end.x)
            top = min(line.start.y, line.end.y)
            bottom = max(line.start.y, line.end.y)

            points = []
            if right - left == 0:
                for y in range(top, bottom + 1):
                    points.append(Point(left, y))
            elif line.end.y - line.start.y == 0:
                for x in range(left, right + 1):
                    points.append(Point(x, top))

            self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])

def draw_rects(rects):
    print("\n\n -- Drawing some stuff ---\n")
    for rc in rects:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == "__main__":
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw_rects(rs)