from colorama import Fore, Back, Style


def is_odd_even(a):
    if a % 2 == 0:
        print(f'{a} is an even number' + Fore.RED + '!' + Style.RESET_ALL)
    else:
        print(f'{a} is an odd number' + Fore.RED + '!' + Style.RESET_ALL)


if __name__ == '__main__':
    a = int(input('Number to check'))
    is_odd_even(a)
