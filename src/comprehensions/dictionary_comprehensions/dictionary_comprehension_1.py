roll_numbers = [122, 233, 353, 456]
names = ['alex', 'bob', 'can', 'don']
new_dictionary = {i: j for (i, j) in zip(roll_numbers, names)}
print(new_dictionary)
