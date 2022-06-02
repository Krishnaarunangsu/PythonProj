# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A.isdisjoint(B))
print(A.difference(B))
print(frozenset({1, 2}))
print(A | B)
print(frozenset({1, 2, 3, 4, 5, 6}))
print(A.add(3))

# https://www.programiz.com/python-programming/set
