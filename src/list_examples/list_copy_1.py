x = ["1", "2", "3", "4"]
print(type(x))
numbers = list(x)
numbers_1 = x
x[0] = "0"
print(numbers[0])  # numbers array will not be affected
print(numbers_1[0])
print(x[0])
