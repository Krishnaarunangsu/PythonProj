roll_numbers = [122, 233, 353, 456]
names = ['alex', 'bob', 'can', 'don']

new_dictionary = {i: j for (i, j) in zip(roll_numbers, names)}
print(f'Dictionary-1:{new_dictionary}')

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_dictionary_1 = {x: x ** 2 for x in values if x ** 2 % 4 == 0}
print(f'Dictionary-2:{new_dictionary_1}')
