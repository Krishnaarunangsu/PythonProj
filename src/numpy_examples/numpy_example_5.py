# To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists.
import numpy as np

numpy_array_0 = np.arange(10, 30, 5)
numpy_array_1 = np.arange(0, 2, 0.3)  # it accepts float arguments
print(f'The first numpy array is:{numpy_array_0}')
print(f'The second numpy array is:{numpy_array_1}')
