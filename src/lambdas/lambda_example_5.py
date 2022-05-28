# We can also replace list comprehension with Lambda by using a map() method, not only it is a fast but efficient
# too, and let’s also see how to use lambda in the filter(). filter() and map()


# Python program to demonstrate lambda functions inside map() and filter()


a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]

# in filter either we use assignment or conditional operator, the pass actual parameter will get return
filtered = filter(lambda x: x % 2 == 0, a)
print(list(filtered))

# in map either we use assignment or conditional operator, the result of the value will get returned
mapped = map(lambda x: x % 2 == 0, a)
print(list(mapped))
