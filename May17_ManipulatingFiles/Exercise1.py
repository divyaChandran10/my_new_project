import json


def get_subscribers():
    with open('user.json', 'r') as file:
        data = json.load(file)
    print('\n SUBSCRIBERS \n')
    for users in data:
        if users["is_subscriber"]:
            print(users)


def get_active_users():
    with open('user.json', 'r') as file:
        data = json.load(file)
    print('\n ACTIVE USERS \n')
    for users in data:
        if users["is_active"]:
            print(users)


def get_weak_passwords():
    with open('user.json', 'r') as file:
        data = json.load(file)
    for users in data:
        if (users["password"]).isalpha() or (users["password"]).isnumeric():
            print('\n', users)


def get_number_of_users():
    with open('user.json', 'r') as file:
        data = json.load(file)
    print(f'\n The number of users in the system: {len(data)} \n')


def get_login():
    user_name = input('Enter username \n')
    pass_word = input('Enter password \n')
    count = 0
    with open('user.json', 'r') as file:
        data = json.load(file)
    for users in data:
        if users['username'] == user_name and \
            users['password'] == pass_word:
            count = 1
            if users['is_active'] and users['is_subscriber']:
                print('\n Logged in successfully!!! \n')
            elif not users['is_subscriber']:
                print('***  Please subscribe   ***\n')
            elif users['is_subscriber'] and not users['is_active']:
                print('You are not an active user \n')
    if count != 1:
        print('Invalid credentials\n')


def generate_contact_list():
    with open('user.json', 'r') as file:
        data = json.load(file)
    for user in data:
        print(f'{user["username"]} - {user["email"]}')


if __name__ == '__main__':
    get_subscribers()
    get_active_users()
    get_weak_passwords()
    get_number_of_users()
    get_login()
    generate_contact_list()

