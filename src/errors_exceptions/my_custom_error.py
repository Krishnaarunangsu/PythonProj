class MyCustomError(Exception):
    """
    Custom Exception- User Defined
    """

    def __init__(self, *args):
        """
        Instantiation and Initialization
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        """
        String representation
        :return:
        """
        if self.message:
            return f'My Custom Error:{self.message}'
        else:
            return f'My Custom Error has been raised'


if __name__ == "__main__":
    # raise MyCustomError
    raise MyCustomError('We have a problem')
