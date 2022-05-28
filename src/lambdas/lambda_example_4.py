# Python program to demonstrate
# lambda functions


def power(n):
    return lambda a: a ** n


# base = lambda a : a**2 get returned to base
base = power(2)

print("Now power is set to 2", base)

# when calling base it gets executed with already set with 2
print("8 power of 2 = ", base(8))

# base = lambda a : a**5 get returned to base
base = power(5)
print("Now power is set to 5", base)

# when calling base it gets executed with already set with newly 2
print("8 powerof 5 = ", base(8))
