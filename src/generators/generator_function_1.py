# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simple_generator_fun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simple_generator_fun():
    print(value)
