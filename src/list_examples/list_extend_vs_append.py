a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# Extend unpacks the iterable and then adds the elements to the list
a1.extend(b)
print(f'Modified List after the extend:{a1}')

# Append adds the original iterable
a2.append(b)
print(f'Modified List after the append:{a2}')
