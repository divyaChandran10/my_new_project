def get_string():
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    con_string = '-inator'
    one_string = input('Enter the string')
    len1 = str(len(one_string))
    if one_string.count(' ') > 0:
        print('Only one word string is allowed.', end=' ')
        get_string()
    elif one_string.endswith(vowels):
        one_string1 = one_string + con_string + ' ' + len1 + '000'
        print(f'inatorInator("{one_string}")  -->  "{one_string1}"')
    elif not one_string.endswith(vowels):
        one_string2 = one_string + con_string.strip('-') + ' ' + len1 + '000'
        print(f'inatorInator("{one_string}")  -->  "{one_string2}"')


if __name__ == '__main__':
    get_string()
