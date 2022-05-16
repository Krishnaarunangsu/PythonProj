# Python code to demonstrate example of
# hierarchical inheritance

class Details:
    """
    Details Class : Parent Class
    """

    def __init__(self):
        """

        """
        self.__id = None
        self.__name = None
        self.__gender = None

    def set_data(self, id, name, gender):
        """

        :param id:
        :param name:
        :param gender:
        :return:
        """
        self.__id = id
        self.__name = name
        self.__gender = gender

    def show_data(self):
        """

        :return:
        """
        print("Id: ", self.__id)
        print("Name: ", self.__name)
        print("Gender: ", self.__gender)


class Employee(Details):  # Inheritance
    """
    Employee Class : Inherited from Details Class
    """

    def __init__(self):
        self.__company = None
        self.__dept = None

    def set_employee(self, id, name, gender, comp, dept):
        """

        :param id:
        :param name:
        :param gender:
        :param comp:
        :param dept:
        :return:
        """
        self.set_data(id, name, gender)
        self.__company = comp
        self.__dept = dept

    def show_employee(self):
        """

        :return:
        """
        self.showData()
        print("Company: ", self.__company)
        print("Department: ", self.__dept)


class Doctor(Details):  # Inheritance
    """
    Doctor Class: Inherited from Details Class
    """

    def __init__(self):
        """

        """
        self.__hospital = None
        self.__dept = None

    def set_employee(self, id, name, gender, hos, dept):
        """

        :param id:
        :param name:
        :param gender:
        :param hos:
        :param dept:
        :return:
        """
        self.setData(id, name, gender)
        self.__hospital = hos
        self.__dept = dept

    def show_employee(self):
        """

        :return:
        """
        self.show_data()
        print("Hospital: ", self.__hospital)
        print("Department: ", self.__dept)


def main():
    """
    main method to coordinate the activities
    :return:
    """
    print("Employee Object")
    e = Employee()
    e.setEmployee(1, "Prem Sharma", "Male", "gmr", "excavation")
    e.showEmployee()
    print("\nDoctor Object")
    d = Doctor()
    d.setEmployee(1, "pankaj", "male", "aiims", "eyes")
    d.showEmployee()


if __name__ == "__main__":
    main()
