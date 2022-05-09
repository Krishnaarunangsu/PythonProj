# Python program to demonstrate
# overriding in multiple inheritance


# Defining parent class 1
class Parent1:
    """

    """

    def __init__(self):
        """

        """

    # Parent's show method
    def show(self):
        """
        Display Parent 1
        :return:
        """
        print(f"Inside Parent1:{self}")


# Defining Parent class 2
class Parent2:
    """

    """

    def __init__(self):
        """

        """

    # Parent's show method
    def display(self):
        """
        Display Parent 2
        :return:
        """
        print(f'Inside Parent 2:{self}')


# Defining child class
class Child(Parent1, Parent2):

    # Child's show method
    def show(self):
        print(f"Inside Child:{self}")


# Driver's code
obj = Child()

obj.show()
obj.display()
