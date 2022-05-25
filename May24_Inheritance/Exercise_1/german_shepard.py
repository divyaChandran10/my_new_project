from May24_Inheritance.Exercise_1.dog import Dog


class GermanShepard(Dog):

    # TODO: override the walk() method
    def walk(self):
        super().walk()
        print('German Shepard`s show their beautiful fur while running.')
