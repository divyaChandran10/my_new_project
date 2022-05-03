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


modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]


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
            print(f'You did not complete module {module__name}')
    elif not user:
        print(f'You did not complete module {module__name}')


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


def has_no_requirement(modulename):
    no_requirement = None
    for modules_list in modules:
        #print(modules_list.get("requirement"))
        if modules_list['name'] == modulename and not modules_list.get("requirement"):
            no_requirement = True
            break
        else:
            no_requirement = False
    return no_requirement


def meets_requirement(user, modulename):
    meet_requirement = None
    for modules_list in modules:
        if has_no_requirement(modulename):
            meet_requirement = True
            break
        elif has_no_requirement(modulename) and check_module(user, modulename) and (modules_list['completed'] for
                                                                                    modules_list in user['modules']):
            meet_requirement = True
            break
        else:
            meet_requirement = False
    return meet_requirement


def may_enroll(username, password, modulename):
    enroll_value = None
    user = get_user_v2(username, password)
    if user and user['type'] == 'Student' and not check_module(user, modulename):
        enroll_value = True
    elif not user and has_no_requirement(modulename):
        enroll_value = True
    elif not user and not has_no_requirement(modulename):
        enroll_value = False
    else:
        enroll_value = False
    return enroll_value


if __name__ == '__main__':
    username = input("What is your username? ")
    password = input(f"Type the password for username {username}: ")
    modulename = input("What module do you want to check? ")
    show_registration(username, password, modulename)
    has_completed_module(username, password, modulename)
    if may_enroll(username, password, modulename):
        print(f"You may register to the module {modulename}.")
    else:
        print(f"You may not register to the module {modulename}.")
    has_no_requirement(modulename)


