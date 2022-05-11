class Person:
    age = 25

    @classmethod
    def print_age(cls):
        print('The age is:', cls.age)


# create printAge class method
Person.print_age()
