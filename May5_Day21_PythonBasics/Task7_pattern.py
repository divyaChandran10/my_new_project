from colorama import Fore, Back, Style

if __name__ == '__main__':
    symbol = input('Enter any sign for the pattern')
    symbol = symbol + "  "
    print(Fore.RED + f'{symbol}\n{(2 * symbol)}\n{(3 * symbol + "")}\n{(4 * symbol)}\n{(5 * symbol)}')
    print(f'{(4 * symbol)}\n{(3 * symbol)}\n{(2 * symbol)}\n{symbol}')

    # pattern print using for loop
    for i in range(0, 5):
        for j in range(0, i):
            print("* ", end=' ')
        print(" ")
    for i in range(4, 0, -1):
        for j in range(0, i-1):
            print("* ", end=' ')
        print(" ")
