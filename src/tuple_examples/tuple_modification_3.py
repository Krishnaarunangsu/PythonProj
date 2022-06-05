# Deleting a Tuple
# As discussed above, we cannot change the elements in a tuple.
# It means that we cannot delete or remove items from a tuple.
# Deleting a tuple entirely, however, is possible using the keyword del.

# Deleting tuples
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
print(my_tuple)
