# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# A set cannot have mutable elements like lists, sets or dictionaries as its elements.
# my_set = {1.0, "Hello", (1, 2, 3), {1, 7}}
my_set = {1.0, "Hello", (1, 2, 3), {"id": 1, "age": 7}}
print(my_set)
