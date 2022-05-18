# A Python program to generate squares from 1 sto 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def next_square():
    i = 1

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in next_square():
    if num > 100:
        break
    print(num)
