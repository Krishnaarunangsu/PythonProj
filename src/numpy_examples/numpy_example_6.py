# When arange is used with floating point arguments, it is generally not possible to predict the number of elements
# obtained, due to the finite floating point precision. For this reason, it is usually better to use the function
# linspace that receives as an argument the number of elements that we want, instead of the step:

import numpy as np
from numpy import pi

numpy_array_0 = np.linspace(0, 2, 9)  # 9 numbers from 0 to 2 array([ 0. , 0.25, 0.5 , 0.75, 1. , 1.25, 1.5 , 1.75,
numpy_array_1 = np.linspace(0, 2 * pi, 100)  # useful to evaluate function at lots of ˓→points
numpy_array_2 = np.sin(numpy_array_1)

print(f'The first numpy array is:{numpy_array_0}')
print(f'The second numpy array is:{numpy_array_1}')
print(f'The third numpy array is:{numpy_array_2}')
