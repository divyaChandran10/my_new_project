class Companies:

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    # def __str__(self):
    #     return f'{self.name}-->{self.owner}'

    def __repr__(self):
        return f'Name:{self.name}--> Owner:{self.owner}'


if __name__ == '__main__':
    c = Companies('Lufthansa', 'ABC')

    # print objects without __str__ and __repr__ method
    # print as mentioned in __str__ method even __repr__ method is implemented
    # print as mentioned in __repr__ method when __str__ is not implemented
    print(c)

    # print objects without __str__ and __repr__ method
    # print as mentioned in __str__ method even __repr__ method is implemented
    # print as mentioned in __repr__ method when __str__ is not implemented
    print(f'{c}')
