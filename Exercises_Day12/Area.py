def area_rectangle():
    area_rec = base_a * base_b
    print(f'Area of rectangle is {area_rec}')


def area_circle():
    pi = 3.14
    area_cir = pi * height_c * height_c
    print(f'Area of circle is {area_cir}')


def area_trapezium():
    area_trap = ((base_a + base_b) / 2) * height_c
    print(f'Area of trapezium is {area_trap}')


def area_square():
    area_sqr = 4 * base_b
    print(f'Area of square is {area_sqr}')


def area_triangle():
    area_tri = 1/2 * base_a * height_c
    print(f'Area of triangle is {area_tri}')


if __name__ == '__main__':

    print('Enter the base value 1')
    base_a = int(input())

    print('Enter the base value 2')
    base_b = int(input())

    print('Enter the height value ')
    height_c = int(input())

    print('Calls all the functions')
    area_rectangle()

    area_circle()

    area_square()

    area_triangle()

    area_trapezium()
