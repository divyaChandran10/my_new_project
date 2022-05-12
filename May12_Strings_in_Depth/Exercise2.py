from colorama import Fore, Style
import colorama

if __name__ == '__main__':
    #  Task 1
    text = 'Berlin is a world city of culture, politics, media and science.'
    print(len(text))

    #  Task 2
    print(f'{text[0]} {text[-1]}')

    #  Task 3
    print(f'{text[0:3].upper()}')

    #  Task 4
    text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital "
    count = text.count('B')
    print(f'B appears: {count}' + Fore.BLUE + ' times' + Style.RESET_ALL)

    #  Task 5
    text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the " \
           "western borough of Spandau."
    last_10_char = text[-10:]
    print(last_10_char)

    #  Task 6
    text = "---Python programming---"
    strip_text = text.strip('-')
    print(strip_text)

    #  Task 7
    first_name = 'Divya'
    last_name = 'Chandran'
    f_name = 'Firstname' + ': ' + first_name
    l_name = 'Lastname' + ': ' + last_name
    print(f'{f_name}\n{l_name}')



