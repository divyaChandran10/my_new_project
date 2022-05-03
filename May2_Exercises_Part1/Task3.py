import datetime


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
#today = datetime.date(2021, 8, 8)
today = datetime.date(2021, 8, 7)
#today = datetime.date(2021, 8, 9)

# Your code here


def is_weekend(date):
    if (date.weekday()) == 5 or (date.weekday()) == 6:
        return True
    else:
        return False


if __name__ == '__main__':
    print(today.weekday())
    if (username == valid.get('username') and password == valid.get('password')) or is_weekend(today):
        print(f'Welcome, {username}!')
    elif (username == valid.get('username') and password == valid.get('password')) and (is_weekend(today) == 'False'):
        print(f'Welcome, {username}!')
    else:
        print('Credentials are invalid')
