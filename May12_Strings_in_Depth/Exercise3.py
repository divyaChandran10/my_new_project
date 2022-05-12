if __name__ == '__main__':
    secret = input('*secret:*')
    name = input('*name:*')
    year = input('*year:*')

    concat_string = secret + name
    rev_concat_string = concat_string[::-1]
    # First way
    secret_code = rev_concat_string + year
    print(secret_code)

    # second way
    print(f'{rev_concat_string}{year}')
