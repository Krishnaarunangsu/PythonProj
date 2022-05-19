def function_decorator(func):
    def wrapped_func():
        print('=' * 30)
        print(func)
        func()
        print('=' * 30)

    return wrapped_func


# Then, let’s use this decorator.
@function_decorator
def test():
    print('Hello World!')


test()
