# Delete an user-defined object

class MyClass:
    a = 10

    def func(self):
        print(f'Hello:{self}')


# Output:
print(MyClass)

# deleting MyClass
del MyClass

# Error: MyClass is not defined
print(MyClass)
