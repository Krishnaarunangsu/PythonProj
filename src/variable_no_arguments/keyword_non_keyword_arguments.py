# Python program to illustrate *kwargs for variable number of keyword arguments
class KeyWordNonKeywordArguments:
    """

    """

    def __init__(self):
        """

        """

    @staticmethod
    def my_function(*args, **kwargs):
        print("args: ", args)
        print("kwargs: ", kwargs)


# Driver code
KeyWordNonKeywordArguments.my_function('geeks', 'for', 'geeks', first='Geeks', mid='for', last='Geeks')
print('******************************')
# KeyWordNonKeywordArguments.my_function(first='Amit', second='Eliza', third='Jennifer', fourth='Alan')
