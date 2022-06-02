# Referencing and copyingYou can copy variables using the =
# sign.
a = 1
b = a
print(b)

# When you change the initial variable, the copy will not be affected.
a = 1
b = a
a = 2
print(b)

# Lists are an exception to this rule. Using the =sign creates a reference to the first list, rather than a copy.
# This means that when you change the initial list, the new list will change as well.
a = [1, 2]
b = a
a[0] = 2
print(b)

# To create an independent copy of the list, you need to slice it [:]or placeit inside the list()function. The lists
# band c, are unaffected by the changes made to a, as they were copied before the changes were made.
a = [1, 2]
b = a[:]
c = list(a)
a[0] = 2
print(a, b, c)
