import numpy as np
import pandas as pd

year_data = {
    'stats': pd.Series(np.arange(10, 15, 1.0)),
    'year': pd.Series(["2012", "2007", "2012", "2003"]),
    "intake": pd.Series(["SUMMER", "WINTER", "WINTER", "SUMMER"]),
}

year_data_df = pd.DataFrame(year_data)
print(f'The year statistics is:{year_data_df}')
