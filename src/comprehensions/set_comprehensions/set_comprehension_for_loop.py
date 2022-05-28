# with for loop
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
new_set = set()

for element in my_set:
    new_set.add(element ** 2)

print("The existing set is:")
print(my_set)

print("The Newly Created set is:")
print(f'For Loop:{new_set}')

print('************************************************')
# With for loop
new_set = {element ** 2 for element in my_set}

print("The Newly Created set is:")
print(f'With Set Comprehension:{new_set}')
