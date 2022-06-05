import numpy as np

a = np.array([2, 3, 4])
print(f"The array is:{a}")
print(f'The dtype of the array is:{a.dtype}')
b = np.array([1.2, 3.5, 5.1])
print(f"The array is:{b}")
print(f'The dtype of the array is:{b.dtype}')
c = np.array([1.2, 3.5, 5.1, 7])
print(f"The array is:{c}")
print(f'The dtype of the array is:{c.dtype}')

a = np.array(1, 2, 3, 4)  # WRONG
a = np.array([1, 2, 3, 4])  # RIGHT
