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


def get_user_v2(in_username, in_password):
    for user in users:
        if {in_username, in_password} == {user['name'], user['password']}:
            return user
    return None


def check_module(user, module_name):
    module_value = None
    for modules_list in user['modules']:
        if module_name == modules_list['title']:
            module_value = True
            break
        else:
            module_value = False
    return module_value


def has_completed_module(user__name, pass__word, module__name):
    condition = None
    user = get_user_v2(user__name, pass__word)
    if user and user['type'] == 'Student':
        for modules_list in user['modules']:
            #print(modules_list['completed'])
            if modulename == modules_list['title'] and modules_list['completed']:
                condition = True
                break
            else:
                condition = False
        if condition:
            print(f'You have completed the module {module__name}')
        else:
            print(f'You did not complete {module__name}')
    elif not user:
        print(f'You did not complete {module__name}')


def show_registration(user_name, pass_word, module_name):
    user = get_user_v2(user_name, pass_word)
    if user and user['type'] == 'Student':
        if check_module(user, module_name):
            print(f'You are registered to the module {module_name}')
        else:
            print(f'You did not register to the module {module_name}')
    elif not user:
        print(f'You did not register to the module {module_name}')
    else:
        print('You are a teacher')


if __name__ == '__main__':
    show_registration(username, password, modulename)
    has_completed_module(username, password, modulename)
