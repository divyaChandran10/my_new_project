class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def __add__(self, other):
        return self.area() + other.area()


if __name__ == '__main__':
    square1 = Square(2)
    square2 = Square(3)

    # magic method __add__ must be implemented to use any operator for objects
    print(square1 + square2)
