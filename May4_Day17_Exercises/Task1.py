roles = {
    "ST": "Student",
    "REST": "Registered student",
    "AL": "Alumni",
    "AN": "Anonymous",
    "TE": "Teacher",
    "AD": "Admin"
}

users = [
    {
        "name": "Holly",
        "role": roles["ST"]
    },
    {
        "name": "Peter",
        "role": roles["ST"]
    },
    {
        "name": "Luke",
        "role": roles["ST"]
    },
    {
        "name": "Janis",
        "role": roles["TE"]
    },
    {
        "name": "Aretha",
        "role": roles["TE"]
    },
    {
        "name": "Ringo",
        "role": roles["AD"]
    }
]

modules = [
    {
        "title": "Computer basics",
        "teacher": "Janis",
        "registered": ["Peter"],
        "alumni": ["Luke", "Holly"]
    },
    {
        "title": "Python basics",
        "teacher": "Janis",
        "registered": ["Holly"],
        "alumni": [],
        "requirement": "Computer basics"
    },
    {
        "title": "Django basics",
        "teacher": "Aretha",
        "registered": [],
        "alumni": [],
        "requirement": "Python basics"
    }
]

module_permissions = {
    roles["AN"]: ["describe"],
    roles["ST"]: ["describe"],
    roles["REST"]: ["describe", "read", "comment"],
    roles["AL"]: ["describe", "read"],
    roles["TE"]: ["describe", "read"],
    roles["AD"]: ["describe", "read", "write", "comment"]
}


def is_registered(username, modulename):
    #return_value = None
    for user in users:
        if user['name'] == username:
            for module in range(len(modules)):
                if modules[module]['title'] == modulename:
                    # print(module['registered'])
                    if username in modules[module]['registered']:
                        return True
    return False


def is_alumni(username, modulename):
    for user in users:
        if user['name'] == username:
            for module in range(len(modules)):
                if modules[module]['title'] == modulename:
                    if username in modules[module]['alumni']:
                        return True
    return False


def has_permission(username, modulename, permission):
    for user in users:
        if user['name'] == username and user['role'] == 'Student':
            if permission in module_permissions['Student']:
                return True
            elif is_registered(username, modulename):
                if permission in module_permissions['Registered student']:
                    return True
            elif is_alumni(username, modulename):
                if permission in module_permissions['Alumni']:
                    return True
        elif user['name'] == username and user['role'] == 'Teacher':
            if permission in module_permissions['Teacher']:
                return True
            else:
                for module in range(len(modules)):
                    if modules[module]['title'] == modulename and modules[module]['teacher'] == username:
                        return True
        elif user['name'] == username and user['role'] == 'Admin':
            return True
        elif permission in module_permissions['Anonymous']:
            return True
    return False


if __name__ == '__main__':
    for permission in module_permissions["Admin"]:
        for module in modules:
            print(f"Can {permission.upper()} on {module['title'].upper()}?")
            print("Anonymous",
                  has_permission("Somebody", module["title"], permission))
            for user in users:
                print(user["name"],
                      has_permission(user["name"], module["title"], permission))
