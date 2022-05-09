class Person:
    """

    """

    # Initialization
    def __init__(self, firstname='Milaan', lastname='Parmar', age=96, country='England', city='London'):
        """

        :param firstname:
        :param lastname:
        :param age:
        :param country:
        :param city:
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    # instance method
    def show_person_info(self):
        """

        :return:
        """
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'


p1 = Person()
print(p1.person_info())
p2 = Person('Ben', 'Doe', 30, 'Finland', 'Tamper')
print(p2.show_person_info())
