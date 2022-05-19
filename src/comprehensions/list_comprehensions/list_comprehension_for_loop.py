# With for loop
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

# With List Comprehension
h_letters = [letter for letter in 'human']
print(h_letters)

# With Lambda function
h_letters = list(map(lambda x: x, 'human'))
print(h_letters)
