class Shape:
    """

    """

    def __init__(self, length: float, breadth: float):
        """

        :param length:
        :param breadth:
        """
        self.length = length
        self.breadth = breadth

    def calculate(self):
        """

        :return:
        """
        return self.length * self.breadth

    def calculate(self):
        """

        :return:
        """
        return 2 * self.length * self.breadth


shape = Shape(5, 4)
print(shape.calculate())
