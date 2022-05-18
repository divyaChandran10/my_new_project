class User:
    def __init__(self):
        self.name = None
        self.address = None

    def update_data(self, name):
        self.name = name


user1 = User()
user2 = User()

user1.name = 'Divya'
user2.name = 'Larmika'
user1.update_data('Sanjit')
print(user1.name)
print(user2.name)
