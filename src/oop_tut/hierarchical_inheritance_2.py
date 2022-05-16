class Student:
    """
    Parent Class
    """

    def __init__(self):
        """

        """
        self.__name = input("Name: ")
        self.__roll_no = input("Roll Number: ")

    def get_student_info(self):
        pass

    def put_student(self):
        print(f"fRoll Number : {self.__rollno} and Name : {self.__name}")


class BScStudent(Student):
    """

    """

    def __init__(self):
        super().__init__()
        self.__m = int(input("Maths Marks: "))
        self.__c = int(input("Chemistry Marks: "))
        self.__p = int(input("Physics Marks: "))

    def get_bsc(self):
        self.get_student_info()

    def put_bsc(self):
        self.put_student()
        print(f"Marks is Subjects:{self.__p},{self.__c},{self.__m}")


class BAStudent(Student):
    """

    """

    def __init__(self):
        super().__init__()
        self.__e = int(input("Economic Marks: "))
        self.__g = int(input("Geography Marks: "))
        self.__h = int(input("History Marks: "))

    def get_ba(self):
        """

        :return:
        """
        self.get_student_info()

    def put_ba(self):
        """

        :return:
        """
        self.put_student()
        print("Marks is Subjects ", self.__h, self.__g, self.__e)


def main():
    """
    main method to coordinate the activities
    :return:
    """
    print("Enter Bsc Student's details")
    student1 = BScStudent()
    student1.get_bsc()
    student1.put_bsc()

    print("Enter Ba Student's details")
    student2 = BAStudent()
    student2.get_ba()
    student2.put_ba()


if __name__ == "__main__":
    main()
