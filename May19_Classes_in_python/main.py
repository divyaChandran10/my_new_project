from user import UserManager


if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user('Div', 'St. 10', 'div@gmail')

    print(user_manager.get_number_of_users())

    user_info = user_manager.get_user_by_name('Div')
    print(user_info.address)

    option = -1

    while option != 0:
        print('Please select an operation')
        print('1. Add user \n 2. remove user \n 3. List users')
        option = int(input('Enter the option'))
        if option == 1:
            name = input('enter name')
            address = input('enter address')
            email = input('enter email')
            user_manager.add_user(name, address, email)
        elif option == 2:
            email = input('enter email')
            user_manager.remove_user(email)
        elif option == 3:
            users = user_manager.get_all_users()
            for user in users:
                print(user.name)
            print(len(user))

