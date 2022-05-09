from colorama import Fore, Style


if __name__ == '__main__':
    temperature = float(input(Fore.BLUE + 'Input the value of temperature you' + Style.RESET_ALL + '\'d like to convert:'))
    shortcut = input('Input the scale shortcut you\'' + Fore.BLUE + 'd like to convert (F - Fahrenheit, C - Celsius: ' + Style.RESET_ALL).upper()
    if shortcut in ('C', 'c'):
        print('The temperature' + Fore.RED + " in " + Style.RESET_ALL + 'Fahrenheit is', (temperature * (9/5) + 32), 'degrees')
    elif shortcut in ('F', 'f'):
        print('The temperature' + Fore.RED + " in " + Style.RESET_ALL + 'Celsius is', (temperature-32)*(5/9), 'degrees')
    else:
        print(f'Invalid conversion')

    #  Alternate way , takes input in any case and converts to upper case

    shortcut = input('Input the scale shortcut you\'' + Fore.BLUE + 'd like to convert (F - Fahrenheit, C - Celsius: ' + Style.RESET_ALL).upper()
    if shortcut == 'C':
        print('The temperature' + Fore.RED + " in " + Style.RESET_ALL + 'Fahrenheit is', (temperature * (9/5) + 32), 'degrees')
    elif shortcut == 'F':
        print('The temperature' + Fore.RED + " in " + Style.RESET_ALL + 'Celsius is', (temperature-32)*(5/9), 'degrees')
    else:
        print(f'Invalid conversion')
