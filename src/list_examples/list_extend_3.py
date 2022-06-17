# the + operator

a = [1, 2]
b = [3, 4]

# a += b  # a = a + b

# Output: [1, 2, 3, 4]
# print('a =', a)

f = lambda x, y: x + y
print(f'Value:{f}')
print(f'Value-2:{f(a, b)}')
