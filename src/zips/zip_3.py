from itertools import zip_longest

L1 = [1, 2, 3, 4, 5]
L2 = ['a', 'b', 'c', 'd']

zipL_L1L2 = zip_longest(L1, L2)

print(list(zipL_L1L2))
