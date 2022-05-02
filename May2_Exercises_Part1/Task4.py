users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")


# Rest of your code here


def get_user(x, y):
    for user in users:
        if user['name'] == username and user['password'] == password:
            return user
            #user_value = True
            #print(user_value)
    return None


def get_user_v2(username, password):
    for user in users:
        if {username, password} == {user['name'], user['password']}:
            return user
    return None


if __name__ == '__main__':
    user = get_user(username, password)
    print(user)
    if not user:
        print('An error occurred. You are not authorized..')

    user2 = get_user_v2(username, password)
    if not user2:
        print('An error occurred. You are not authorized..')
