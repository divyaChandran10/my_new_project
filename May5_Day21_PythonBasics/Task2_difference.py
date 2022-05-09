def difference(a, b):
    if a > b:
        print(f'Second number:{a}')
        print(f'Third number:{b}')
        print(f'The result of calculation is:{2 * (a - b)}')
    elif a == b:
        print(f'First number:{a}')
        print(f'Second number:{b}')
        print(f'The result of calculation is:{a - b}')
    else:
        print(f'First number:{a}')
        print(f'Second number:{b}')
        print(f'The result of calculation is:{b - a}')


if __name__ == '__main__':
    a = int(input('Enter a value'))
    b = int(input('Enter b value'))
    difference(a, b)
