# We can also add a new row using the DataFrame.append() function

import pandas as pd

dict_data = {
        'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths': [87, 91, 97, 95],
        'Science': [83, 99, 84, 76]
}

df = pd.DataFrame(dict_data)
print(f'Original Dataframe:\n{df}')

new_record = {
        'Name': 'Amy',
        'Maths': 89,
        'Science': 93
}
df = df.append(new_record, ignore_index=True)

print(f'Modified Dataframe:\n{df}')
