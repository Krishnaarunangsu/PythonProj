# Python program to illustrate *kwargs for variable number of keyword arguments
class KeyWordArguments:
    """

    """

    def __init__(self):
        """

        """

    @staticmethod
    def my_function(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}:{value}")

    # Python program to illustrate  **kwargs for variable number of keyword arguments with one extra argument.
    @staticmethod
    def my_function_2(arg1, **kwargs):
        print(f'First Argument:{arg1}')
        print('#########################')
        for key, value in kwargs.items():
            print(f"{key}, {value}")


# Driver code
KeyWordArguments.my_function(first='Geeks', mid='for', last='Geeks')
print('******************************')
KeyWordArguments.my_function(first='Amit', second='Eliza', third='Jennifer', fourth='Alan')
print('******************************')
KeyWordArguments.my_function_2("Hi", first='Geeks', mid='for', last='Geeks')
print('******************************')
KeyWordArguments.my_function_2("Hello", first='Amit', second='Eliza', third='Jennifer', fourth='Alan')
