def function_decorator(func):
    def wrapped_func(*args, **kwargs):
        print('=' * 30)
        func(*args, **kwargs)
        print('=' * 30)

    return wrapped_func


@function_decorator
def greeting(name):
    print(f'Hey {name}! Good Morning!')


greeting('Krishna')
