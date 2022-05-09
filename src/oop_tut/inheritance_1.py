# Python program to demonstrate
# method overriding


# Defining parent class
class Parent:

    # Constructor
    def __init__(self, age):
        """

        """
        self.value = "Inside Parent"
        self.age = age

    # Parent's show method
    def show(self):
        """

        :return:
        """
        print(self.value)

    def show_details(self):
        """
        Show Parent Details
        :return:
        """
        print(f'Age:{self.age}')


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self, age: float, salary: float):
        """

        :param age:
        :param salary:
        """
        self.value = "Inside Child"
        self.age = age
        self.salary = salary

    # Child's show method
    # def show(self):
    #     print(self.value)
    # def show_details(self):
    #     """
    #     Show Parent Details
    #     :return:
    #     """
    #     print(f'Age:{self.age}')
    #     print(f'Age:{self.salary}')


# Driver's code
obj1 = Parent(45)
obj2 = Child(15, 5000)

obj1.show()
obj1.show_details()
obj2.show()
obj2.show_details()
