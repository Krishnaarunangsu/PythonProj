# Python program to demonstrate
# overriding in multiple inheritance


# Defining parent class 1
class Parent1:
    """
    Parent 1 Class
    """

    def __init__(self):
        """
         Initialization
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
     Parent 2 Class
    """

    def __init__(self):
        """
         Initialization
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
        """
        Show of Child
        :return:
        """
        print(f"Inside Child:{self}")


# Driver's code
obj = Child()

obj.show()
obj.display()
