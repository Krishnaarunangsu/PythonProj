# Import pandas package
import pandas as pd

# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

# Using 'Address' as the column name and equating it to the list
# df2 = df.assign(address=address)
df = df.assign(address=address)

# Observe the result
print(df)
