# Sort the list using key
# take first element for sort
def take_first(elem):
    return elem[0]


# take second element for sort
def take_second(elem):
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=take_first)
# print list
print('Sorted list with first element:', random)

# sort list with key
random.sort(key=take_second)

# print list
print('Sorted list with second element:', random)
