people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

# 1st way of iterating a dictionary
for key, value in people.items():
    print("\nPerson ID:", key)
    print("Person Details:", value)
    print("\n")
    print("Person Details without braces")
    # Get the nested Values
    for key_nested in value:
        print(key_nested + ':', value[key_nested])

# 2nd way of iterating a dictionary
for key_value in people.items():
    print(f'Person Id:{key_value[0]}: Person Details:{key_value[1]}')
