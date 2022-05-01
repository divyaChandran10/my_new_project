def add_positive(a_list):
    j = 0
    for x in a_list:
        if x > 0:
            j = j + 1
    print(f'{j} positive values')


if __name__ == '__main__':
    a = []
    i = 0
    for i in range(0, 6):
        print('Enter any number')
        a.append(int(input()))
    add_positive(a)
    print(a)
