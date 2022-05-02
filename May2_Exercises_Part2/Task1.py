users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")


def get_user_v2(username, password):
    for user in users:
        if {username, password} == {user['name'], user['password']}:
            return user
    return None


def check_module(user, module_name):
    for modules_list in user['modules']:
        if module_name == modules_list['title']:
            #print(f'You are registered to the module {modulename}')
            module_value = True
            break
        else:
            module_value = False
    return module_value


def show_registration(username, password, modulename):
    user = get_user_v2(username, password)
    if user and user['type'] == 'Student':
        if check_module(user, modulename):
            print(f'You are registered to the module {modulename}')
        else:
            print(f'You did not register to the module {modulename}')
    elif not user:
        print(f'You did not register to the module {modulename}')
    else:
        print('You are a teacher')


if __name__ == '__main__':
    show_registration(username, password, modulename)
