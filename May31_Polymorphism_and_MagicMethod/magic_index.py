# class Data:
#     def __index__(self):
#         return 2
#
#
# if __name__ == '__main__':
#     x = Data()
#     print(bin(2))
#     print(bin(x))
#     print(hex(x))


class My_Integer:
    def __init__(self, i):
        self.i = i

    def __index__(self):
        return self.i
        #return 'str'

    def __int__(self):
        return int(self.i)

    @classmethod
    def __del__(cls):
        print('deleted class objects')
        #cls.__del__()
        #pass


class Animal:
    def __init__(self, i):
        self.i = i

    def __index__(self):
        return self.i


if __name__ == '__main__':

    x = My_Integer(1)
    #x = 1
    y = My_Integer(8)
    ss = int(My_Integer(4.9))  #  Class object converted to integer by invoking __int__ method
    z = My_Integer(3)
    my_list = [1, 'div', 3, 4, 'mon', 6, 7, 8, 9, 10, int(Animal(199))]
    print(my_list[x])  # Class object passed as index (by calling __index__ method , returns integer)
    # 2
    print(my_list[y])
    # 9
    print(my_list[x:y:z])  # in a range 1 : 8 prints value in a list with step value 3
    # [2, 5, 8]
    print(my_list[::])
    print(ss)
    My_Integer.__del__()
