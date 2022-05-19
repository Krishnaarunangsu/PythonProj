my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("The existing set is:")
print(my_set)
my_set = {element for element in my_set if element % 2 == 0}
print("The modified set is:")
print(my_set)

# Change the data type of elements of the set We can also change the data types of the elements of a set using set
# comprehension as shown in the following example. Here, we have converted all the integer elements of a set to
# strings.
#
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
new_set = {str(element) for element in my_set}
print("The existing set is:")
print(my_set)
print("The Newly Created set is:")
print(new_set)
