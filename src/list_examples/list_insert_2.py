# inserting a Tuple (as an Element) to the List
# List with different data types
mixed_list = [1, 'TCG', True, {1, 2}, [5, 6, 7]]
print(f'The List is:{mixed_list}')

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list in the nd position
mixed_list.insert(1, number_tuple)

print('Updated List:', mixed_list)

mixed_list[5].insert(3, 9)
print('Updated List:', mixed_list)
