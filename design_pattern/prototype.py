import copy


class Shape:
    def __init__(self, id):
        self.id = id

    def clone(self):
        return copy.copy(self)

    def __str__(self):
        return f"Shape ID: {self.id}"

class Circle(Shape):
    def __init__(self, id, radius):
        super().__init__(id)
        self.radius = radius

    def __str__(self):
        return f"Circle(ID: {self.id}, Radius: {self.radius})"

class Rectangle(Shape):
    def __init__(self, id, width, height):
        super().__init__(id)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(ID: {self.id}, Width: {self.width}, Height: {self.height})"

# Usage
circle1 = Circle(1, 10)
print(circle1)  # Output: Circle(ID: 1, Radius: 10)

circle2 = circle1.clone()
circle2.id = 2
circle2.radius = 15
print(circle2)  # Output: Circle(ID: 2, Radius: 15)

rectangle1 = Rectangle(3, 20, 30)
print(rectangle1)  # Output: Rectangle(ID: 3, Width: 20, Height: 30)

rectangle2 = rectangle1.clone()
rectangle2.id = 4
rectangle2.width = 25
rectangle2.height = 35
print(rectangle2)  # Output: Rectangle(ID: 4, Width: 25, Height: 35)
