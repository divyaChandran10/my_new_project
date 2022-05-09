if __name__ == '__main__':

    list1 = [2, 3, 3, 4, 3, 2, 1, 3]
    print(list1)
    list2 = [2, 3, 3, 4, 3, 2, 1, 3]
    print(list2)
    number = int(input('Enter the value to remove from list1'))
    while number in list1:
        list1.remove(number)
    print(list1)
    # num = int(input('Enter the value to remove from list2'))
    # x = len(list2)
    # for i in range(x-1):
    #     print(i)
    #     if list2[i] == num:
    #         list2.remove(num)
    #         x = x - 1
    #         #continue
    # print(list2)
