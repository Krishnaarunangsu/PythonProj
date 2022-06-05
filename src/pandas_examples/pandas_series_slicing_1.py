import numpy as np
import pandas as pd

data = np.array([1, 2, 3, 4, 5, 6])
series_1 = pd.Series(data)
print(series_1[0:3])
print(series_1[:3])
print(series_1[3:5])
print(series_1[3:3])
