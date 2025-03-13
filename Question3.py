# Define the base class Shape
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def calculate_area(self):
        # Base class area method does nothing
        pass

# Define the derived class Rectangle
class Rectangle(Shape):
    def __init__(self, color, filled, width, height):
        # Call the Shape class's constructor using super()
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def calculate_area(self):
        # Calculate and return the area of the rectangle
        return self.width * self.height

# Create a Rectangle object
rectangle = Rectangle("red", True, 4, 5)

# Print the rectangle's properties
print(f"Color: {rectangle.color}")
print(f"Filled: {rectangle.filled}")
print(f"Width: {rectangle.width}")
print(f"Height: {rectangle.height}")
print(f"Area: {rectangle.calculate_area()}")