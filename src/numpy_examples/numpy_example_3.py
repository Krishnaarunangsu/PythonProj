# array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into
# three-dimensional arrays, and so on.
import numpy as np

# numpy_array_1 = np.array([1.5, 2, 3], [4, 5, 6])
numpy_array_1 = np.array([(1.5, 2, 3), (4, 5, 6)])
print(f'The numpy array is:\n{numpy_array_1}')

# The type of the array can also be explicitly specified at creation time:
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(f'The Numpy array is:{c}')
