# 1. Tuple Membership Test
# We can test if an item exists in a tuple or not, using the keyword in.

# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple)
print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)

# 2. Iterating Through a Tuple
# We can use a for loop to iterate through each item in a tuple.

# Using a for loop to iterate through a tuple
for name in ('John', 'Kate'):
    print("Hello", name)
