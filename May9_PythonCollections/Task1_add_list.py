if __name__ == '__main__':
    l1 = [2, 3, 4, 5, 8, 10]
    l2 = [9, 4, 3, 9, 3, 1]
    l3 = []
    l4 = []
    l5 = []
    for item1, item2 in zip(l1, l2):
        l3.append(item1 + item2)
    print(l3)

    for index in range(len(l1)):
        l4.append(l1[index] + l2[index])
    print(l4)

    for index in range(len(l1)):
        total = l1[index] + l2[index]
        l5.append(total)
    print(l5)
