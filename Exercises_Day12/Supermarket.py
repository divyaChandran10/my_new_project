import sys


def get_section(var1, var2, var3):
    amount = 0
    #print(f'The values are {var1}, {var2}, {var3}')
    if var1 >= 1 and var2 >= 1 and var3 >= 1:
        print("####   All sections are visited   #####")
        print(f'Value of each products are {total}')
        for i in total:
            amount = amount + i
        print(f'The final amount to be paid: {amount}')
        sys.exit()
    else:
        print("*** Sections ***")
        print("1.grocery\n2.milk_product\n3. stationary")
        n = int(input("Which section do u want to enter?\n"))
        m = n
        if m == 1:
            if var1 == 1:
                print("!!!! Cannot re enter the section---- Choose another section !!!!")
                get_section(var1, var2, var3)
            else:
                grocery(var1, var2, var3)
        elif m == 2:
            if var2 == 1:
                print("!!!! Cannot re enter the section---- Choose another section !!!!")
                get_section(var1, var2, var3)
            else:
                milk_products(var1, var2, var3)
        elif m == 3:
            if var3 == 1:
                print("!!!! Cannot re enter the section---- Choose another section !!!!")
                get_section(var1, var2, var3)
            else:
                stationary(var1, var2, var3)
        else:
            print("Invalid section number")
            get_section(var1, var2, var3)


def grocery(x, y, z):
    g1 = 20
    g2 = 30
    print("Choose one product\n")
    print("1.vegetables\n2.Fruits \n")
    p1 = int(input())
    var1 = x + 1
    if p1 == 1:
        print(f'The value of chosen product is{g1}')
        total.append(g1)
        get_section(var1, y, z)
    elif p1 == 2:
        print(f'The value of chosen product is{g2}')
        total.append(g2)
        get_section(var1, y, z)
    else:
        print(f'Invalid option: Choose the correct option')
        grocery(var1, y, z)
    return var1, y, z


def milk_products(x, y, z):
    m1 = 10
    m2 = 20
    print("Choose one product\n")
    print("1.Milk\n2. Yoghurt\n")
    p1 = int(input())
    var2 = y + 1
    if p1 == 1:
        print(f'The value of chosen product is{m1}')
        total.append(m1)
        get_section(x, var2, z)
    elif p1 == 2:
        print(f'The value of chosen product is{m2}')
        total.append(m2)
        get_section(x, var2, z)
    else:
        print(f'Invalid option: Choose the correct option')
        milk_products(x, var2, z)
    return x, var2, z


def stationary(x, y, z):
    s1 = 10
    s2 = 20
    print("Choose one product\n")
    print("1.Pen\n2. Pencil\n")
    p1 = int(input())
    var3 = z + 1
    if p1 == 1:
        print(f'The value of chosen product is{s1}')
        total.append(s1)
        get_section(x, y, var3)
    elif p1 == 2:
        print(f'The value of chosen product is{s2}')
        total.append(s2)
        get_section(x, y, var3)
    else:
        print(f'Invalid option: Choose the correct option')
        stationary(x, y, var3)
    return x, y, var3


if __name__ == '__main__':
    global var1
    var1 = 0
    global var2
    var2 = 0
    global var3
    var3 = 0
    global total
    total = []
    get_section(var1, var2, var3)
