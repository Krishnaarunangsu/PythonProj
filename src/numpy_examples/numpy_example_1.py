import numpy as np

array_1 = np.arange(15).reshape(3, 5)
print(f'The numpy array is:\n{array_1}')
print(f'The dimension of the array is:{array_1.ndim}')
print(f'The shape of the array is:{array_1.shape}')
print(f'The size of the array is:{array_1.size}')
print(f'The dtype of the array is:{array_1.dtype.name}')
print(f'The type of the array is:{type(array_1)}')
print(f'The item size of the array is:{array_1.itemsize}')
