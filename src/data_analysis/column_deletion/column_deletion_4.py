# Remove all columns between a specific column to another column.

# Import pandas package
import pandas as pd

# create a dictionary with five fields each
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

print(f'Original Dataframe:\n{df}')

# Remove all columns between column index 1 to 3
df.drop(df.iloc[:, 1:3], inplace=True, axis=1)

print(f'Modified Dataframe:\n{df}')
