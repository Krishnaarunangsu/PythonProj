# Sort the list using key
# take second element for sort
def take_second(elem):
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=take_second)

# print list
print('Sorted list:', random)
