# Method Overloading By Using Multiple Dispatch Decorator
# Multiple Dispatch Decorator Can be installed by: pip3 install multipledispatch

from multipledispatch import dispatch


class PythonOverload:
    """

    """

    def __init__(self):
        """
        Initialization
        """
        self.result = 0

    @dispatch(int, int)
    def product(self, first, second):
        """

        :param first:
        :param second:
        :return:
        """
        self.result = first * second
        return self.result

    @dispatch(int, int, int)
    def product(self, first, second, third):
        """
         Passing two pa
        :param first:
        :param second:
        :param third:
        :return:
        """

        self.result = first * second * third
        return self.result

    # you can also pass data type of any value as per requirement
    @dispatch(float, float, float)
    def product(self, first, second, third):
        """
        Passing three parameters
        :param first:
        :param second:
        :param third:
        :return:
        """
        self.result = first * second * third
        return self.result


# calling product method with 2 arguments
product(2, 3)  # this will give output of 6
product(2, 3, 2)  # this will give output of 12
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997
