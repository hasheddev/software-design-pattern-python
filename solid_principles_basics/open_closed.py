from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

#Voilates principle of adding functionality be extension and  not by modification
#open for extension, closed for modification
note="""modification means changing existing code to add features, while extension means adding new code without touching what already works."""
class ProductFilter:
    def filter_by_color(self, products: list[Product], color: Color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products: list[Product], size: Size):
        for p in products:
            if p.size == size:
                yield 

#modifying already tested code to extend functionality is not the best method
#This also causes state space explosion as we can also filter by or   2^n -1
    def filter_by_size_and_color(self, products: list[Product], size: Size, color: Color):
        for p in products:
            if p.size == size and p.color == color:
                yield 
#access by for loop or convert to list list(filter) or user next(filter())

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other): #use for &
        return AndSpecification(self, other)

    def __or__(self, other): #use for |
        return OrSpecification(self, other)

class Filter:
    def filter(self, items, spec: Specification):
        pass

class ColorSpecificaton(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecificaton(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *specs: Specification):
            self.specs = specs
    
    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.specs)

class OrSpecification(Specification):
    def __init__(self, *specs: Specification):
            self.specs = specs
    
    def is_satisfied(self, item):
        return any(spec.is_satisfied(item) for spec in self.specs)

#create andspec orspec  e.t.c
class DataFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("house", Color.BLUE, Size.LARGE)
    products = [apple, tree, house]
    print("**OLD**")
    for p in ProductFilter().filter_by_color(products, Color.GREEN):
        print(f"{p.name} is {p.color}")
    print("**NEW**")
    spec = ColorSpecificaton(Color.GREEN)

    for p in DataFilter().filter(products, spec):
        print(f"{p.name} is {p.color}")
    large_spec = SizeSpecificaton(Size.LARGE)
    blue_spec = ColorSpecificaton(Color.BLUE)
    and_spec = AndSpecification(large_spec, blue_spec)
    #and_spec = large_spec & blue_spec
    print("***Large blue***")
    for p in DataFilter().filter(products, and_spec):
        print(f"{p.name} is {p.color} and {p.size}")