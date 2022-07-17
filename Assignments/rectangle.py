class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)


my_rectangle = Rectangle(2, 3)
my_rectangle.area()