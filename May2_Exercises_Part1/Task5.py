users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")


def get_user_v2(username, password):
    for user in users:
        if {username, password} == {user['name'], user['password']}:
            return user
    return None


def show_offers(username, password):
    user = get_user_v2(username, password)
    #if (user and user['type'] == 'Student') or not user:
    if not user or user['type'] == 'Student':
        print('We have great courses to offer you')


if __name__ == '__main__':
    show_offers(username, password)

