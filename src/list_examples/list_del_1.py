# Emptying the List Using del

# Defining a list
list_1 = [{1, 2}, 'a', ['1.1', '2.2']]
print(f'The list is:{list_1}')

# Copy the list to another list
list_2 = list_1

# clearing the list
# del list_1[:]

# deleting the original list object
del list_1

print(f'The list after deletion is:{list_1}')
# print(f'The other list after deletion of the original list is:\n{list_2}')
