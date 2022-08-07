# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop()

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

# pop() parameters The pop() method takes a single argument (index). The argument passed to the method is optional.
# If not passed, the default index -1 is passed as an argument (index of the last item). If the index passed to the
# method is not in range, it throws IndexError: pop index out of range exception.
