# create a list
prime_numbers = [2, 3, 5]

# create another list
numbers = [1, 4]

# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)

print('List after extend():', numbers)

# Output: List after extend(): [1, 4, 2, 3, 5]

# languages list
languages = ['French', 'English']

# another list of language
languages1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
languages.extend(languages1)

print('Languages List:', languages)
