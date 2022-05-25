import sys

from canvas import Canvas
from shapes import Rectangle, Triangle, Square
from shapes import Pentagon, Circle


if __name__ == '__main__':
    canvas = Canvas()

    circle1 = Circle(2)
    rectangle1 = Rectangle(5, 4)
    rectangle2 = Rectangle(9, 76)
    print(str(rectangle1 == rectangle2))
    square1 = Square(2)
    triangle1 = Triangle(4, 5, 6)
    pentagon1 = Pentagon(3)

    canvas.add_shape(circle1)
    canvas.add_shape(rectangle1)
    canvas.add_shape(square1)
    canvas.add_shape(triangle1)
    canvas.add_shape(pentagon1)

    canvas.print()
    #canvas.remove_shape(circle1)
    #canvas.remove_shape(rectangle1)
    #canvas.remove_shape(square1)

    #canvas.print()
    #print('*** All shapes removed ***')
    option = -1
    while option != 0:
        option = int(input('1. Add shape\n2.Remove shape\n3.Print Canvas\n4.Exit\nEnter the option'))
        if option == 1:
            shape_name = input('1. circle\n2. Rectangle\n3.Square\n4.Triangle\n5.Pentagon\nEnter the name of the shape')
            if shape_name.lower() == 'circle':
                radius = int(input('enter the radius'))
                circle = Circle(radius)
                canvas.add_shape(circle)
            elif shape_name.lower() == 'rectangle':
                width = int(input('Enter the width'))
                height = int(input('enter the height'))
                rectangle = Rectangle(width, height)
                canvas.add_shape(rectangle)
            elif shape_name.lower() == 'square':
                side = int(input('enter the side'))
                square = Square(side)
                canvas.add_shape(square)
            elif shape_name.lower() == 'triangle':
                pass
        elif option == 2:
            count = 0
            shape_name = input('Enter the name of the shape\n1. circle\n2. Rectangle\n3.Square\n4.Triangle\n5.Pentagon')
            #if shape_name.lower() == 'circle':
            for item in canvas.shapes:
                #print(type(item), '\n')
                #print(type(item).__name__, '\n')
                if type(item).__name__.lower() == shape_name.lower():
                    print(item, '\n')
                    canvas.remove_shape(item)
                    count = 1
            if count != 1:
                print('Item not available in the list\n')
                #break
        elif option == 3:
            canvas.print()
        elif option == 4:
            sys.exit()
