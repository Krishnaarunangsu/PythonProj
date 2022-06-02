# Add Elements of Tuple and Set to List

# languages list
languages = ['French']

# languages tuple
languages_tuple = ('Spanish', 'Portuguese')

# languages set
languages_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
languages.extend(languages_tuple)

print('New Language List:', languages)

# appending language_set elements to language
languages.extend(languages_set)

print('Newer Languages List:', languages)
