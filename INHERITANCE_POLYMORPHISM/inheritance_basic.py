# INHERITANCE
class shape:
    def area(self):
        return 0
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
rec1=rectangle(10,7)
print("Area of rectangle:",rec1.area())

circle1=circle(5)
print("Area of circle:",circle1.area())

