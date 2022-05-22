import math

from check import print_rectangle_properties


class Rectangle:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def get_area(self):
        return float(self.width * self.height)

    def get_perimeter(self):
        return float(2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return float(math.sqrt(self.width ** 2 + self.height ** 2))

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


def main():
    rec1 = Rectangle(9.0, 12.0)
    print_rectangle_properties(rec1)
    rec2 = Rectangle(17.0, 13.0)
    print_rectangle_properties(rec2)


if __name__ == "__main__":
    main()
