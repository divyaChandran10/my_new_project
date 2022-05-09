from colorama import Fore, Back, Style


if __name__ == '__main__':
    #ran_number = 6
    print(f'Guess a number between 1 and 10 ' + Fore.RED + 'until' + Style.RESET_ALL, 'you get it right:')
    guess_number = int(input())
    while guess_number != 5:
        print(f'Guess a number between 1 and 10 ' + Fore.RED + 'until' + Style.RESET_ALL, ' you get it right:')
        guess_number = int(input())
    print('Well guessed ' + Fore.RED + '!' + Style.RESET_ALL)
