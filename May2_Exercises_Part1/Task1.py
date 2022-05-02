# Validate the input credentials of a user


if __name__ == '__main__':

    username = input("What is your username? ")
    password = input(f"Type the password for username {username}: ")
    valid = {"username": "admin", "password": "admin"}

    print(valid.get('username'))
    if username == valid.get('username') and password == valid.get('password'):
        print(f'Welcome, {username}!')
    else:
        print('Credentials are invalid')
