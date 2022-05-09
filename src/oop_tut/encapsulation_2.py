# Example 2: Data Encapsulation in Python

class Employee:
    def __init__(self, name):
        self.name = name
        self.__salary = 500

    def show(self):
        print("Name is ", self.name, "and salary is", self.__salary)


# Outside class
E = Employee("Bella")
# E.PrintName()
print(E.name)
# print(E.PrintName())
print(E.__salary)
