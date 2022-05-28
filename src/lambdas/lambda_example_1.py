# Python program to demonstrate lambda functions

# lambda returns a function object
add = lambda letter: letter + "for Geeks "
print(add('Friday '))

# Add 10 to argument a, and return the result:
f = lambda a, b: a + b
print(f'Value:{f}')
print(f'Value-2:{f(5, 7)}')

# Lambda functions can take any number of arguments:
# Multiply argument a with argument b and return the result:
x = lambda a, b: a * b
print(x(5, 6))

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
