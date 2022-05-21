from shopping import ShoppingCart


class User:

    def __init__(self):
        self.name = None
        self.address = None
        self.email = None
        self.password = None
        self.shopping_cart = ShoppingCart()

    def update_data(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    def pick_a_product(self, product):
        self.shopping_cart.add_product(product)


class UserManager:

    def __init__(self):
        self.users = []

    def add_user(self, name, address, email):
        user = User()
        user.update_data(name, address, email)
        self.users.append(user)

    def remove_user(self, email):
        for user in self.users:
            if user.email == email:
                self.users.remove(user)

    def get_all_users(self):
        return self.users

    def get_number_of_users(self):
        return len(self.users)

    def get_user_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user


user_manager = UserManager()

# print(len(user_manager.get_all_users()) + 3)  # 0
print(user_manager.get_number_of_users())  # 0

user_manager.add_user("mathias", "somestr. 9", "mail@mathias.example")

# print(len(user_manager.get_all_users()))  # 1
print(user_manager.get_number_of_users())  # 1
