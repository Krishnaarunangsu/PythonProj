import pandas as pd

df = pd.read_csv("..\\data\\data.csv")

# print the first 5 records of the dataframe
print(f' First 5 records of the dataframe:\n{df.head()}')

# print the first 10 records of the dataframe
print(f' First 5 records of the dataframe:\n{df.head(n=10)}')

print(f'Dataset Columns:\n{df.columns}');

# print the last 5 records of the dataframe
print(f' Last 5 records of the dataframe:\n{df.tail()}')

# Checking the types of data in each column
print(f'Data types of the columns:\n{df.dtypes}')

# Shape of the dataframe
print(f'Shape of the dataframe:\n{df.shape}')

# Size of the dataframe
print(f'Size of the dataframe:\n{df.size}')

# Total Rows in the dataframe
print(f'Total Rows in the Dataframe:\n{df.count()}')

# Total Duplicate Rows in the dataframe
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

print(df.groupby(['Model']).count())

# Drop/Delete Duplicate Rows
df = df.drop_duplicates()
print(df.head(5))

print(df.groupby(['Model']).count())

# Total Rows in the dataframe
print(f'Total Rows in the Dataframe after removing the Duplicates:\n{df.count()}')
