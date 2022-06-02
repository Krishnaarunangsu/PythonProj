# initialize my_set
my_set = {1, 3}
print(my_set)

# my_set[0]
# if you uncomment the above line you will get an error
# TypeError: 'set' object does not support indexing

# add an element
my_set.add(2)
print(my_set)

# add multiple elements
my_set.update([2, 3, 4])
print(my_set)

# add list and set check if the duplicate elements are getting added or not
my_set.update([4, 5], {7, 6, 8})
print(my_set)
