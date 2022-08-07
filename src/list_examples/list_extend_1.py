# create a list
prime_numbers = [2, 3, 5]

# create another list
numbers = [1, 4]

# add all elements of prime_numbers to numbers
numbers.append(prime_numbers)

print('List after extend():', numbers)

# languages list
languages = ['French', 'English']

# another list of language
languages_1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
languages.extend(languages_1)

print('Languages List:', languages)
