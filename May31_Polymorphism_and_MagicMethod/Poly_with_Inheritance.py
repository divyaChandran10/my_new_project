class Animal:
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def info(self):
        pass
        #print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        pass
        #print("Dogs Bark")


class Cat(Animal):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def info(self):
        print(f"I am a cat.")

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def info(self):
        print(f"I am a dog.")

    def make_sound(self):
        print("Bark")


if __name__ == '__main__':
    cat = Cat()
    dog = Dog()
    #animal = Animal()
    animals = [cat, dog]
    for i in animals:
        i.make_sound()
        i.info()


