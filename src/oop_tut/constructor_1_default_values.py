# Program to illustrate method overloading
class Edpresso:
    """
     Class to call a person
    """

    def __init__(self, id: int = 7):
        """
        Initialization
        :param id:
        """
        self.id = id

    def hello(self, name=None):
        """
        Calling a person
        :param name:
        :return:
        """
        if name is not None:
            print('Hello ' + name + " " + "ID" + ":" + str(self.id))
        else:
            print('Hello ')


# Create an instance
obj = Edpresso()

# Call the method without parameter
obj.hello()

# Call the method with a parameter
obj.hello('Kadambini')

# object with value
obj = Edpresso(9)
obj.hello('Kadambini')
