# Often, the elements of an array are originally unknown, but its size is known. Hence, NumPy offers several
# functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays,
# an expensive operation.
# The function zeros creates an array full of zeros, the function ones creates an array full
# of ones, and the function empty creates an array whose initial content is random and depends on the state of the
# memory. By default, the dtype of the created array is float64.
import numpy as np

numpy_zero_array = np.zeros((3, 4))  # 3*4 array
numpy_ones_array = np.ones((2, 3, 4), dtype=int)

print(f'The numpy zero array is:\n{numpy_zero_array}')
print(f'The numpy ones array is:\n{numpy_ones_array}')

# Creation of the empty array
numpy_empty_array = np.empty((2, 3, 4))
print(f'The empty array is:{numpy_empty_array}')
