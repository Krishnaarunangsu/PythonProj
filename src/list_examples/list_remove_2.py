# remove() method on a list having duplicate elements

# If a list contains duplicate elements, the remove() method only removes the first matching element.

# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' is removed
animals.remove('dog')

# Updated animals list
print('Updated animals list: ', animals)
