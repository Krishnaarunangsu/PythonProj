# We can also add a new row using the DataFrame.append() function

import pandas as pd

dict_data = {
        'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths': [87, 91, 97, 95],
        'Science': [83, 99, 84, 76]
}

df1 = pd.DataFrame(dict_data)
print(f'Original Dataframe-1:\n{df1}')

new_records = {
        'Name': ['Amy', 'Maddy'],
        'Maths': [89, 90],
        'Science': [93, 81]
}

df2 = pd.DataFrame(dict)
print(f'Original Dataframe-2:\n{df1}')

df3 = pd.concat([df1, df2], ignore_index=True)
df3.reset_index()

print(f'Modified Dataframe:\n{df3}')
