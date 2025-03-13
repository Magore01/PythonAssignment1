# Define an abstract base class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define a Circle class that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Define a function to calculate the total area of shapes
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

# Create a list of shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(2, 8)
]

# Calculate and print the total area
print("Total area:", total_area(shapes))