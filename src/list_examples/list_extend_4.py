# the list slicing syntax
a = [1, 2]
b = [3, 4]

a[len(a):] = b

# Output: [1, 2, 3, 4]
print('a =', a)
