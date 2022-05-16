# Creating a Base class named University:

class University:
    """
    University: Parent Class
    """

    def __init__(self):
        """

        """
        print('Constructor of the Base Class')
        # Initializing a class variable named univ to store university name:
        self.univ = "MIT"

    def display(self):
        """
        Method to print the University Name
        :return:
        """
        print(f"The University name is: {self.univ}")


class Course(University):
    """
    Course: Child Class of University
    """

    def __init__(self):
        """
        Constructor
        """
        # using "super" keyword to access members of the parent class having same name:
        print("Constructor of the Child Class 1 of Class University")
        University.__init__(self)
        self.course = "CSE"

    def display(self):
        """
        Method to print the Course Name
        :return:
        """
        # using "super" keyword to access display method defined in the parent class:
        print(f"The Course name is: {self.course}")
        University.display(self)


# 2nd Derived or Child Class of University Class:
class Branch(University):
    """

    """

    def __init__(self):
        """
        Constructor
        """
        print("Constructor of the Child Class 2 of Class University")
        self.branch = "Data Science"

    def display(self):
        """
        Method to print the Branch Name
        :return:
        """
        print(f"The Branch name is: {self.branch}")


# Derived or Child Class of Class Course and Branch:
class Student(Course, Branch):
    def __init__(self):
        print("Constructor of Child class of Course and Branch is called")
        self.name = "Tonny"
        Branch.__init__(self)
        Course.__init__(self)

    def display(self):
        print(f"The Name of the student is: {self.name}")
        Branch.display(self)
        Course.display(self)


def main():
    """
    Coordinate the activities
    :return:
    """
    ob = Student()  # Object named ob of the class Student.
    print()
    ob.display()  # Calling the display method of Student class.


if __name__ == "__main__":
    main()
