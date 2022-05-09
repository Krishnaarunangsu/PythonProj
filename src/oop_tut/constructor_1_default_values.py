# Program to illustrate method overloading
class Edpresso:
    """

    """

    def __init__(self, id: int = 7):
        """

        :param id:
        """
        self.id = id

    def hello(self, name=None):
        """

        :param name:
        :return:
        """
        if name is not None:
            print('Hello ' + name + " " + "ID" + ":" + str(self.id))
        else:
            print('Hello ')


# Create an instance
obj = Edpresso()

# Call the method wiyhout parameter
obj.hello()

# Call the method with a parameter
obj.hello('Kadambini')

# object with value
obj = Edpresso(9)
obj.hello('Kadambini')
