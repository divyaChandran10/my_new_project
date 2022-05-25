import math
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * pi * self.radius

    def print_summary(self):
        print(f'*** Circle ***\nRadius: {self.radius}\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}')


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return pi * self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def print_summary(self):
        print(f'*** Rectangle ***\nWidth: {self.width}\nHeight: {self.height}\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}')

    def __eq__(self, other):
        if self.width == other.width and self.height == other.height:
            return True
        return False


class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side

    def print_summary(self):
        print(f'*** Square ***\nSide: {self.side}\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}')


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        s_p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s_p * (s_p - self.side1) * (s_p - self.side2) * (s_p - self.side3))

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def print_summary(self):
        print(f'*** Triangle ***\nSides: {self.side1},{self.side2},{self.side3}\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}')


class Pentagon:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(self.side, 2)) / 4.0

    def get_perimeter(self):
        return 5 * self.side

    def print_summary(self):
        print(f'*** Pentagon ***\nSide: {self.side}\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}')
