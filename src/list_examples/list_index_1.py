animals = ["cat", "dog", "rabbit", "horse"]
print(animals.index("dog"))

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')

print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'p' is vowels
# index = vowels.index('p')

print('The index of p:', index)

# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'e' in alphabets
index = alphabets.index('e')

print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)  # 6

print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)  # Error!

print('The index of i:', index)
