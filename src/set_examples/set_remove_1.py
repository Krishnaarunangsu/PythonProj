# Difference between discard() and remove()
# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
my_set.discard(4)
print(my_set)

# remove an element
my_set.remove(6)
print(my_set)

# discard an element not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element not present in my_set
# you will get an error.
# Output: KeyError

my_set.remove(2)
