# create a list
prime_numbers = [11, 2, 3, 5, 7, 9, 11]

# remove 9 from the list
try:
    prime_numbers.remove(11)
except ValueError as ve:
    print(ve)

# Updated prime_numbers List
print('Updated List: ', prime_numbers)
