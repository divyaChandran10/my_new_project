import math


def area_circle(radius):
    area_of_circle = math.pi * radius * radius
    print(f'The area of the circle with radius {radius} is: {area_of_circle:.2f}')


if __name__ == '__main__':
    radius = float(input('Input th radius of the circle:'))
    area_circle(radius)
