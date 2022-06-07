class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self, length, width):
        print(length*width)


my_rectangle = Rectangle(0, 0)
my_rectangle.area(2, 3)
