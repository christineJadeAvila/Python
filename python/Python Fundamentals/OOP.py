class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area = self.height * self.width
        return area

rect1 = Rectangle(12, 10)

print(type(rect1))

print(rect1.height)
print(rect1.width)
print(rect1.area())

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius * self.radius)
        return area

circle1 = Circle(4)

print(circle1.radius)
print(circle1.area())
