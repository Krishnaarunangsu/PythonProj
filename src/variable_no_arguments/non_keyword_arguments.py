# Python program to illustrate *kwargs for variable number of keyword arguments
class NonKeyWordArguments:
    """

    """

    def __init__(self):
        """

        """

    @staticmethod
    def my_function(*args):
        for arg in args:
            print(f"{arg}")

    # Python program to illustrate *args with first extra argument
    @staticmethod
    def my_function_2(arg1, *argv):
        print("First argument :", arg1)
        for arg in argv:
            print("Next argument through *argv :", arg)


# Driver code
NonKeyWordArguments.my_function('Geeks', 'for', 'Geeks')
print('******************************')
NonKeyWordArguments.my_function('Amit', 'Eliza', 'Jennifer', 'Alan')
print('********************************')
NonKeyWordArguments.my_function_2('Geeks', 'for', 'Geeks')
print('******************************')
NonKeyWordArguments.my_function_2('Amit', 'Eliza', 'Jennifer', 'Alan')
