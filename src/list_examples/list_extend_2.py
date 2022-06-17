# Add Elements of Tuple and Set to List

# languages list
languages = ['French']
print(f'1.The list is:{languages}')

# languages tuple
languages_tuple = ('Spanish', 'Portuguese')
# Extending  language_tuple elements with language
languages.extend(languages_tuple)
print(f'2. Updated Language List after extending with tuple:\n{languages}')

# languages set
languages_set = {'Chinese', 'Japanese'}
# Extending  language_set elements with language
languages.extend(languages_set)
print(f'3. Updated Language List after extending with set:\n{languages}')
