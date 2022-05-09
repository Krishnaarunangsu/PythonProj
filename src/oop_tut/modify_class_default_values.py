class Person:
    def __init__(self, firstname='Milaan', lastname='Parmar', age=96, country='England', city='London'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    # instance method
    def show_person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    # instance method
    def add_skill(self, skill):
        """
        Update default value(skill)
        :param skill:
        :return:
        """
        self.skills.append(skill)
        # return self.skills.append(skill)

    def show_skill(self):
        """

        :return:
        """
        return f'{self.skills}'


p1 = Person()
print(p1.show_person_info())
p1.add_skill('Python')
p1.add_skill('MATLAB')
p1.add_skill('R')
p2 = Person('Ben', 'Doe', 30, 'Finland', 'Tampere')
print(p2.show_person_info())
# print(p1.skills)
# print(p2.skills)
print(p1.show_skill())
print(p2.show_skill())
