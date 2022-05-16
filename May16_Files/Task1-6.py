if __name__ == '__main__':

    #  Task1
    with open('task1.txt') as file:
        print('§§§§§  TASK1 OUTPUT §§§§§')
        print(file.read())

    #  Task2
    with open('task2.txt') as file:
        content = file.readlines()
        #content_list = list(content)
        print('\n §§§§§  TASK2 OUTPUT §§§§§')
        print(len(content) - 2, '\n')  # or 'print(len(lines[2:]))

    #  Task3
    with open('task3.txt') as file:
        print('§§§§§  TASK 3 OUTPUT §§§§§')
        print(file.read(), '\n')

    with open('task3.txt') as f:
        content = f.readlines()
        content_list = list(content)
        print('§§§§§  TASK3 OUTPUT §§§§§')
        for even_line in range(len(content_list)):
            if (even_line % 2) == 0:
                print(content_list[even_line], end='')
        for odd_line in range(len(content_list)):
            if (odd_line % 2) != 0:
                print(content_list[odd_line], end='')

    # alternate ways
        #odds = content_list[::2]

    # Task4
    with open('task4.txt') as f:
        print('\n\n', '§§§§§  TASK  4 OUTPUT §§§§§')
        print(f.read()[1622:1635], '\n')  # file.read() returns list

    # Task5
    with open('task5.txt') as f:
        print('§§§§§  TASK  5 OUTPUT §§§§§')
        print(f.readline())
        a = f.readline().strip()   # if char != '\n'
        count = 0
        for char in a:
            count = count + 1
        print(count, '\n')

    #  Task6
    with open('task6.txt') as f:
        print('§§§§§  TASK  6 OUTPUT §§§§§')
        integer_list = []
        content = f.readlines()
        content_list = list(content)
        for line in content_list:
            count = 0
            for char in line:
                count = count + 1
            integer_list.append(count)
        print(integer_list)
