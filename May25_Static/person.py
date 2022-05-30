class Person:

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def set_name(self, name):
        self.name = name

    @staticmethod
    def calculate_age(dob):
        print(dob)
    # TODO


if __name__ == '__main__':
    Person.calculate_age("1-11-1989")  # invokes static method with class name
    p1 = Person('Divya', "1.11.1989")  # other methods with objects
    p1.set_name('div')

