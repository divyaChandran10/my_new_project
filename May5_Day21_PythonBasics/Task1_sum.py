def sum(a, b, c):
    if a == b == c:
        print(f'First number:{a}')
        print(f'Second number:{b}')
        print(f'Third number:{c}')
        print(f'The triple sum is:{3 * (a + b + c)}')
    else:
        print(f'First number:{a}')
        print(f'Second number:{b}')
        print(f'Third number:{c}')
        print(f'The sum is:{a + b + c}')


if __name__ == '__main__':
    a = int(input('Enter a value'))
    b = int(input('Enter b value'))
    c = int(input('Enter c value'))
    sum(a, b, c)
