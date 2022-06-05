# Pandas Series is a one-dimensional labeled array capable of holding
# data of any type (integer, string, float, python objects, etc.).
# The axis labels are collectively called index.
# Pandas Series is nothing but a column in an excel sheet.
# Labels need not be unique but must be a hashable type.

import numpy as np
import pandas as pd
from numpy import int64

# Create series
# 1. Empty Series
series_1 = pd.Series(dtype=int64)
print(f'The Series is:\n{series_1}')

# 2. Create Series from a list
items = [1, 3, 5, 9]
series_2 = pd.Series(items)
print(f'The Series is:\n{series_2}')

# 3. Create Series from a numpy array
data = np.array(['x', 'y', 'z'])
series_3 = pd.Series(data)
print(f'The Series is:\n{series_3}')

# 4. Create Series from a dictionary(dict)
data_country = {'uk': 'United Kingdom', 'fr': 'France'}
series_4 = pd.Series(data_country)
print(f'The Series is:\n{series_4}')
print(f'series_4[0]:{series_4[0]}')

# 5. Set the index or the row label explicitly
series_4.index = ['country_1', 'country_2']
print(f'The Series is:\n{series_4}')
print(f'series_4[1]:{series_4[1]}')

# 6. Set the index or the row label explicitly with list
names_1 = ["Kavi", "Shyam", "Ravi"]
series_5 = pd.Series(names_1, index=[3, 5, 1])
print(f'The Series with Custom Index or Label is:\n{series_5}')

# 7. Set the index or the row label explicitly with numpy array
names_2 = np.array(["Kavi", "Shyam", "Ravi"])
series_6 = pd.Series(names_2, index=[3, 5, 1])
print(f'The Series with Custom Index or Label is:\n{series_6}')
