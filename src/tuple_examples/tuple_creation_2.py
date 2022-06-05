# Creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough.
# We will need a trailing comma to indicate that it is, in fact, a tuple.

my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>
